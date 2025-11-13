from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("company_interface/<str:company_name>", views.company_interface, name="company_interface"),
    path("admin_interface", views.admin_interface, name="admin_interface"),
    path("priceUpdate", views.share_price_update, name="priceUpdate"),
]