from django.urls import path
from . import views

app_name = 'ecom'

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_up_submit', views.sign_up_submit, name='sign_up_submit'),
    path('login', views.login, name='login'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('welcome', views.welcome, name='welcome'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('prod_details/<int:pk>', views.prod_details, name='prod_details'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
]