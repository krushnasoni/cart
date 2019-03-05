from django.urls import path
from . import views

app_name = 'master'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('cat_list', views.cat_list, name='cat_list'),
    path('cat_new', views.cat_new, name='cat_new'),
    path('cat_edit/<int:pk>', views.cat_edit, name='cat_edit'),
]