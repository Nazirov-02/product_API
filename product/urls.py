from django.urls import path
from product import views

urlpatterns = [
    path('product_list',views.ProductList.as_view(),name='product_list'),
    path('product_detail/<int:pk>/',views.ProductDetail.as_view(),name='product_detail'),
]