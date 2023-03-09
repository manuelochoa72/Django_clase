from django.urls import path
from . import views
app_name='polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('hola/',views.holamanuel, name='hola'),
    path('<int:id_pregunta>/detalle/',views.detalle, name='detalle'),
    path('<int:id_pregunta>/resultados/',views.resultados, name='resultados'),
    path('<int:id_pregunta>/votando/', views.votar, name='votar')
]