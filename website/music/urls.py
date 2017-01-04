from django.conf.urls import url
from . import views

#$ sign means go to the default home page of each app

urlpatterns = [
    url(r'^$', views.index, name='index'),

]
