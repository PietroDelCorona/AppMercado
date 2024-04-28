"""
URL configuration for app_mercado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_mercado.views import home
#from .views import home, google_authenticate

urlpatterns = [
    path('', home, name='home'),  # URL para a página inicial
    #path('google-auth/', google_authenticate, name='google_authenticate'), # URL para a página de autenticação
    path('admin/', admin.site.urls),  # URL para a interface de administração do Django
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
