from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from compras import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.inicio, name="inicio"),
    path("proveedores/", include("compras.urls_proveedores")),
    path("compras/", include("compras.urls_compras")),
]
