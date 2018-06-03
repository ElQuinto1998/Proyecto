from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'activity'

urlpatterns = [

url(r'^actividades/$', views.blog_actividad, name='blog_actividad'),
url(r'^actividades/detalles/(?P<id>\d+)/$', views.detalles_actividad, name='detalles_actividad'),
url(r'^actividades/editar/(?P<id>\d+)/$', views.editar_actividad, name='editar_actividad'),
url(r'^actividades/eliminar/(?P<id>\d+)/$', views.eliminar_actividad, name='eliminar_actividad'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)