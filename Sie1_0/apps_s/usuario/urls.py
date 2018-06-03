from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'user'

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^registro/$', views.registro, name='registro'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)