from django.conf.urls import url
from . import views

app_name = 'activity'

urlpatterns = [

url(r'^actividades/$', views.blog_actividad, name='blog_actividad'),

]