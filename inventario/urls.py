from django.urls import path
from .views import inventario_lista, por_producto_view, add_product, delete, update

urlpatterns = [
    path('', inventario_lista, name='inventario_lista'),
    path('producto/<int:pk>/', por_producto_view, name='por_producto'),
    path('producto/agregar/', add_product, name='agregar_producto'),
    path('producto/eliminar/<int:pk>/', delete, name='producto_eliminar'),
    path('producto/actualizar/<int:pk>/', update, name='actualizar_producto'),
]
