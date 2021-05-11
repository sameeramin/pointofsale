"""
Core App URL Configurations
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cities/', views.cities, name="cities"),
    path('customer/', views.customer, name="customer"),
    path('vendor/', views.vendor, name="vendor"),
    path('sale/', views.sale, name="sale"),
    path('sale_return/', views.sale_return, name="sale_return"),
    path('edit_sale/<str:pk>', views.edit_sale, name="edit_sale"),
    path('edit_sale_return/<str:pk>', views.edit_sale_return, name="edit_sale_return"),
    path('purchase/', views.purchase, name="purchase"),
    path('purchase_return/', views.purchase_return, name="purchase_return"),
    path('edit_purchase/<str:pk>', views.edit_purchase, name="edit_purchase"),
    path('edit_purchase_return/<str:pk>', views.edit_purchase_return, name="edit_purchase_return"),
]
