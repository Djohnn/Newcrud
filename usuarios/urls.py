from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user, name="create_user"), 
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
    path('editar/<int:id>', views.editar, name="editar"),

]


