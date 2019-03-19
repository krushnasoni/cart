from django.urls import path
from . import views

app_name = 'master'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('cat_list', views.cat_list, name='cat_list'),
    path('cat_new', views.cat_new, name='cat_new'),
    path('cat_edit/<int:pk>', views.cat_edit, name='cat_edit'),
    path('cat_del/<int:pk>', views.cat_del, name='cat_del'),
    path('prod_new', views.prod_new, name='prod_new'),
    path('prod_edit/<int:pk>', views.prod_edit, name='prod_edit'),
    path('prod_list', views.prod_list, name='prod_list'),
    path('prod_del/<int:pk>', views.prod_del, name='prod_del'),
    path('gallary/<int:pk>', views.gallary, name='gallary'),
    path('gallary_upload', views.gallary_upload, name='gallary_upload'),
    path('delete_image', views.delete_image, name='delete_image'),
    path('cart_details', views.cart_details, name='cart_details'),
]