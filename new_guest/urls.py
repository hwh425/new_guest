"""new_guest URL Configuration

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
from django.urls import path

from sign import views as sign_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_views.index),
    path('index/', sign_views.index),

    path('login_action/', sign_views.login_action),
    path('event_manage/', sign_views.event_manage),
    path('accounts/login/', sign_views.index),
]
