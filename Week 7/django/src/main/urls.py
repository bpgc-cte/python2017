from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^name/(?P<name>[a-z]+)$', views.name),
    url(r'^books/', views.allbooks)
]