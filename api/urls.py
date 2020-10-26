
from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    # users endpoints
    path("users/", views.user_all, name="user_all"),
    path("user/", views.user, name="user"),
    path("user/update/", views.user_update, name="user_update"),
    path("user/delete/", views.user_delete, name="user_delete"),

    # user authentication endpoint
    path("register/", views.user_register, name="register"),

    # tanks endpoints
    path("tank/create/", views.tank_create, name="tank_create"),
    path("tank/update/", views.tank_update, name="tank_update"),
]
