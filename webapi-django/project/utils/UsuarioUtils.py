import glob
import os

from django.conf import settings

def get_fotoUrl(email, request):
	"""
	Busca o caminho para foto de um Usuário
	"""
	if not email:
		return None

	email=email.lower()
	caminho_foto = os.path.join(settings.MEDIA_ROOT, 'perfis', f'{email}.*')
	arquivo_existe = glob.glob(caminho_foto)

	if arquivo_existe:
		foto = os.path.basename(arquivo_existe[0])
		if request:
			return request.build_absolute_uri(f'{settings.MEDIA_URL}/perfis/{foto}')
	return None



def set_fotoUrl(email, arquivo):
	"""
	Salva a foto de um Usuário e remove anteriores caso necessário
	"""
	email = email.lower()
	extensao = arquivo.name.split('.')[-1].lower()
	fotoNova = f'{email}.{extensao}'

	caminho_perfis = os.path.join(settings.MEDIA_ROOT, 'perfis')
	caminho_foto = os.path.join(caminho_perfis, f'{email}.*')
	os.makedirs(caminho_perfis, exist_ok=True)

	for fotoAntiga in glob.glob(caminho_foto):
		try:
			os.remove(fotoAntiga)
		except OSError:
			pass

	caminho_upload = os.path.join(caminho_perfis, fotoNova)
	with open(caminho_upload, 'wb+') as destino:
		for chunk in arquivo.chunks():
			destino.write(chunk)

	return fotoNova
