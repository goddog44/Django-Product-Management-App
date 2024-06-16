from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.test, name='add_product'),
    path('modify/', views.modify, name='modify_product'),
    path('delete/<int:id>/', views.delete, name='delete_product'),
    path('modify/<int:id>/', views.finalupdate, name='update_product'),
    path('id/<int:id>/', views.update, name='id_product'),
    path('final/<int:id>/', views.finalupdate, name='final_product')
]