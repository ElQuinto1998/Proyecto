from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [

    url(r'^$', views.home, name='home'),
   url(r'^registro/$', views.registro, name='registro'),

]