from django.contrib import admin
from django.urls import path
from hola_mundo.views import *
from Paper_SA.views import (index, PostList, 
                                PostDetail, PostCreate, PostUpdate,
                                PostDelete)

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('mis-productos/', mostrar_Productos, name="mis-productos"),
    path('mis-ventas/', mostrar_mis_ventas, name="mis-ventas"),
    path('personas', mostrar_personas, name="personas"),
    path('personas/create', crear_persona, name="personas-create"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    path('post/list', PostList.as_view(), name="post-list"),
    path('post/<pk>/detail', PostDetail.as_view(), name="post-detail"),
    path('post/create', PostCreate.as_view(), name="post-create"),
    path('post/<pk>/update', PostUpdate.as_view(), name="post-update"),
    path('post/<pk>/delete', PostDelete.as_view(), name="post-delete"),
]
