from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.google_login, name="google_login"),
    path("logout/", views.logout_view, name="logout"),
]
