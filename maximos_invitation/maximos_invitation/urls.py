"""maximos_invitation URL Configuration

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
from .views import main_page, handle_rsvp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home_page'),  # Add this for root path
    path('maximos/', main_page, name='home_page'),
    path('maximos/rsvp/', handle_rsvp, name='handle_rsvp'),
]
