from django.conf.urls import url
from . import views

#$ sign means go to the default home page of each app

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/712/
    #(? P<album_id> isrepresenting 712 as a one word and we can use album_id to save a id), 0-9 is a range for id's
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

]
