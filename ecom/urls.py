from django.urls import path
from . import views

app_name = 'ecom'

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_up_submit', views.sign_up_submit, name='sign_up_submit'),
]