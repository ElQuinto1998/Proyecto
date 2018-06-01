from django.conf.urls import url
from . import views

app_name = 'activity'

urlpatterns = [

url(r'^actividades/$', views.blog_actividad, name='blog_actividad'),
url(r'^actividades/editar/(?P<id>\d+)/$', views.editar_actividad, name='editar_actividad'),
url(r'^actividades/eliminar/(?P<id>\d+)/$', views.eliminar_actividad, name='eliminar_actividad'),

]