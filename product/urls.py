from django.urls import path
from product import views

urlpatterns = [
    path('product_list',views.PostListOrCreate.as_view(),name='product_list'),
    path('product_list/<int:pk>/',views.PostDetail.as_view(),name='product_detail'),
]