from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("become-merchant", views.become_merchant, name="become-merchant"),
    path("address-book", views.address_book, name="address-book"),
    path("zones", views.zones, name="get-zones"),
    path("areas", views.areas, name="get-areas"),
]
