from django.urls import path 
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index , name='index'),
    path('admin_dash', views.admin_dash , name='admin_dash'),
]
