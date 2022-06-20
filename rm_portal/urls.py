"""rm_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from console.views import (
    index,
    console, 
    create_client,
    client_list, 
    create_request, 
    client_upload,
    server_error
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('index/login/', index, name='login'),
    path('manager/<int:rm_id>/console', console, name='console'),

    path('manager/<int:rm_id>/create_request/', create_request, name='create_request'),

    path('manager/<int:rm_id>/create_client/', create_client, name='create_list'),
    path('manager/<int:rm_id>/client_list/', client_list, name='client_list'),

    path('<str:client_url>', client_upload, name='client_upload'),
    path('error/', server_error, name='error')
]
