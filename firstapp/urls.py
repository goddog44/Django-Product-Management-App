from django.urls import path
from . import views

#urlconfig

urlpatterns = [
    path('hello/', views.test, name= 'add_product'),
    path('modify/', views.modify, name = 'modify_product' )
]