"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from listings import views

# handler404 = "listings.views.custom_404"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("bands/", views.band_list, name="band-list"),
    path("bands/<int:id>/", views.band_detail, name="band-detail"),
    path("bands/add/", views.band_create, name="band-create"),
    path("bands/<int:id>/change/", views.band_update, name="band-update"),
    path("annonce_list/", views.annonce_list, name="annonce-list"),
    path("annonce_list/<int:id>/", views.annonce_detail, name="annonce-detail"),
    path("annonce/add/", views.annonce_create, name="annonce-create"),
    path("annonce_list/<int:id>/change/", views.annonce_update, name="annonce-update"),
    path("contact-us/", views.contact, name="contact"),
    path("email_sent/", views.email_sent, name="email-sent"),
    path("about-us/", views.about, name="about"),
]
