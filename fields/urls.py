from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^postfield/(?P<data>.*)$', views.postFieldData, name='data')
]
