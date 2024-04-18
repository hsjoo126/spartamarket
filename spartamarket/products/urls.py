from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path("", views.products, name="products"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
]