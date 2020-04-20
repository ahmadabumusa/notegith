from django.conf.urls import url
from . import views

app_name ='noteapp'
urlpatterns = [
    url(r'^$' , views.allnotes , name ='allnotes'),
    #url(r'^(?P<id>\d+)$', views.onenote , name='notedetail')
    url(r'^(?P<slug>[-\w]+)/$', views.onenote , name='notedetail')
]
