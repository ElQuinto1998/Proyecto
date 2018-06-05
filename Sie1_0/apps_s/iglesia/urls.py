from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'user'

urlpatterns = [

    url(r'^iglesias/$', views.iglesia, name='iglesia'),
    url(r'^iglesias/(?P<id_iglesia>\d+)/$', views.detalle, name='detalles'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)