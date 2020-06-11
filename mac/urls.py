"""mac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views as mac_views
from django.contrib.auth import views as auth
from rest_framework.authtoken import views
from user import views as user_view
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('', mac_views.index),
    path('api/',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token,name='api-tokn-auth'),
    path('login/',user_view.Login,name='login'),
    path('logout/',auth.LogoutView.as_view(template_name='index.html'),name='logout'),
    path('register/',user_view.register,name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
