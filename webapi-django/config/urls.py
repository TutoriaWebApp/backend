from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas da API para o frontend (ex: /v1/usuarios/)
    path('v1/', include('project.urls.api')),

    # Rotas do dashboard HTML para admins (ex: /dashboard/conquistas/)
    path('dashboard/', include('project.urls.dashboard')),
]
