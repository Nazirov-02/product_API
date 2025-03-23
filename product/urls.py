from django.urls import path
from product import views
from product import customobtainview
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'comments', views.CommentViewSet, basename='comment')
router.register(r'images', views.ImageViewSet, basename='image')

urlpatterns = [
    # path('product_list',views.ProductListOrCreate.as_view(),name='product_list'),
    # path('product_list/<int:pk>/',views.ProductDetail.as_view(),name='product_detail'),
    # path('category_list/',views.CategoryListOrCreate.as_view(),name='category_list'),
    # path('category_list/<int:pk>/',views.CategoryDetail.as_view(),name='category_detail'),
    # path('comment_list/',views.CommentListOrCreate.as_view(),name='comment_list'),
    # path('comment_list/<int:pk>/',views.CommentDetail.as_view(),name='comment_detail'),
    # path('img_list/',views.ImageListOrCreate.as_view(),name='img_list'),
    # path('img_list/<int:pk>/',views.ImageDetail.as_view(),name='img_detail'),

    # AuthToken
    # path('login-token/',customobtainview.CustomAuthToken.as_view(),name='custom-token'),
    # path('logout/',customobtainview.CustomLogout.as_view(),name='custom-logout'),

    #JWT
    path('loginJWT/', customobtainview.LoginJWTView.as_view(), name='custom_auth_jwt'),
    path('logoutJWT/',customobtainview.LogoutJWTView.as_view(), name='custom_auth_logout'),

]

urlpatterns += router.urls