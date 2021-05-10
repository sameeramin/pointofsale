"""
Core App URL Configurations
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cities/', views.cities, name="cities"),
    path('sale/', views.sale, name="sale"),
    path('edit_sale/<str:pk>', views.edit_sale, name="edit_sale"),
]
