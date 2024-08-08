from os import name
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("inventario/", include("inventario.urls")),
    path("", auth_views.LoginView.as_view(template_name = "inventario_sistema/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "inventario_sistema/logout.html"), name="logout"),
]