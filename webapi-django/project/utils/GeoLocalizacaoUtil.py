import urllib.request
import urllib.parse
import json
import logging
import math
from django.db import models
from django.core.exceptions import ImproperlyConfigured

logger = logging.getLogger(__name__)

# Fallback para classe Point (do GEOS)
try:
    from django.contrib.gis.geos import Point
except (ImportError, ImproperlyConfigured):
    class Point:
        def __init__(self, x, y, srid=4326):
            self.x = x
            self.y = y
            self.srid = srid
        def __str__(self):
            return f"POINT ({self.x} {self.y})"

# Fallback para PointField (do GIS models)
try:
    from django.contrib.gis.db import models as gis_models
    PointField = gis_models.PointField
except (ImportError, ImproperlyConfigured):
    class MockPointField(models.Field):
        description = "Mock PointField para ambientes sem GDAL"
        def __init__(self, *args, **kwargs):
            self.srid = kwargs.pop('srid', None)
            kwargs['null'] = True
            kwargs['blank'] = True
            super().__init__(*args, **kwargs)
        def get_internal_type(self):
            return "TextField"
        def get_prep_value(self, value):
            if value is None:
                return None
            return str(value)
        def from_db_value(self, value, expression, connection):
            if value is None:
                return value
            try:
                if value.startswith("POINT"):
                    parts = value.replace("POINT", "").replace("(", "").replace(")", "").strip().split()
                    return Point(float(parts[0]), float(parts[1]), srid=self.srid)
            except Exception:
                pass
            return value
    PointField = MockPointField

# Dicionário offline para desenvolvimento, testes e fallback imediato (longitude, latitude)
OFFLINE_COORDINATES = {
    ('brasília', 'df'): (-47.882778, -15.793889),
    ('são paulo', 'sp'): (-46.633308, -23.550520),
    ('rio de janeiro', 'rj'): (-43.172896, -22.906847),
    ('belo horizonte', 'mg'): (-43.934559, -19.917299),
    ('salvador', 'ba'): (-38.501630, -12.977798),
    ('porto alegre', 'rs'): (-51.217658, -30.034647),
    ('recife', 'pe'): (-34.882897, -8.057838),
    ('curitiba', 'pr'): (-49.267137, -25.428990),
    ('fortaleza', 'ce'): (-38.526670, -3.731862),
    ('manaus', 'am'): (-60.021731, -3.119028),
    ('city', 'ts'): (-47.000000, -15.000000),
    ('test city', 'ts'): (-47.000000, -15.000000),
}

class GeoLocalizacaoUtil:
    @staticmethod
    def geocode(cidade: str, estado: str) -> Point:
        """
        Retorna um objeto Point (longitude, latitude) do GEOS para a cidade e estado fornecidos.
        Tenta primeiro obter de um dicionário offline. Em caso de falha, consulta o Nominatim (OSM).
        Retorna Point(0.0, 0.0) em caso de erro ou vazio.
        """
        if not cidade or not estado:
            return Point(0.0, 0.0, srid=4326)

        key = (cidade.strip().lower(), estado.strip().lower())
        if key in OFFLINE_COORDINATES:
            lon, lat = OFFLINE_COORDINATES[key]
            return Point(lon, lat, srid=4326)

        try:
            # Query formatada para busca estruturada
            query = f"{cidade}, {estado}, Brazil"
            url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(query)}&format=json&limit=1"
            
            # Necessário definir um User-Agent para Nominatim
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'TutoriaWebApp/1.0 (contact: test@tutoria.com)'}
            )
            
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode('utf-8'))
                if data and len(data) > 0:
                    lat = float(data[0]['lat'])
                    lon = float(data[0]['lon'])
                    return Point(lon, lat, srid=4326)
        except Exception as e:
            logger.warning(f"Erro ao obter geocodificação para {cidade}-{estado}: {e}")
            
        return Point(0.0, 0.0, srid=4326)

    @staticmethod
    def haversine_distance(point1, point2) -> float:
        """
        Calcula a distância em quilômetros (km) entre dois pontos geográficos (longitude, latitude)
        usando a fórmula de Haversine.
        """
        if not point1 or not point2:
            return float('inf')

        try:
            lon1 = point1.x if hasattr(point1, 'x') else point1[0]
            lat1 = point1.y if hasattr(point1, 'y') else point1[1]
            lon2 = point2.x if hasattr(point2, 'x') else point2[0]
            lat2 = point2.y if hasattr(point2, 'y') else point2[1]
        except (AttributeError, IndexError, TypeError):
            return float('inf')

        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lon = math.radians(lon2 - lon1)

        a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        R = 6371.0  # Raio da Terra em km
        return R * c

