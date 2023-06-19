from . import views
from django.urls import path

from .csv_to_db import get_products

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('list', views.list, name='list'),
    path('fileupload', views.fileupload, name='fileupload'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('ajax/', views.ajax, name='ajax'),
    path('ajax/ajax', views.ajax, name='ajaxpost'),
    path('ajax/delete', views.ajax_delete, name='ajax_delete'),
    path('ajax/getajax', views.getajax, name='getajax'),
    path('register', views.register, name='register'),
    path('register/success/', views.register_success, name='register_success'),
    path('users/', views.users, name='users'),
    path('users/delete/<int:id>', views.user_delete, name='user_delete'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
    path('change_password', views.changePassword, name='changePassword'),
    path('file/delete', views.changePassword, name='changePassword'),
    path('file/delete/<int:id>', views.deleteFiles, name='deleteFiles'),


    path('wishlist/list', views.wishlist, name='wishlist'),
    path('order/list', views.order, name='orderlist'),
    path('buy-product/<int:product_id>', views.buy_product, name='buyProduct'),
    path('add-wishlist/<int:product_id>', views.add_to_wishlist, name='addToWishlist'),

    path('rank-base/', views.rank_based_data, name='rankbase'),

    path('csv_to_db/', get_products, name='get_products'),
]
