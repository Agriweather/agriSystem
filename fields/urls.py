from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^postfields/(?P<data>.*)$', views.postFieldData, name='postdata'),
    url(r'^getfields/(?P<sensor_id>.*)$', views.getFieldData, name='getdata')
]
