from django.conf.urls import url
from . import views

#$ sign means go to the default home page of each app

# app_name deifnes the unique name for this music app. For. if you have detail view for two or more apps, browser will get con
#fused so in order to make it connect with music we use app name
app_name = 'music'

# urlpatterns = [
#     # /music/
#     url(r'^$', views.index, name='index'),
#
#     # /music/album_id/
#     #(? P<album_id> isrepresenting 712 as a one word and we can use album_id to save a id), 0-9 is a range for id's
#     url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
#
#     # url without view,just an action
#     url(r'^(?P<album_id>[0-9]+)/favorites/$', views.favorite, name='favorite'),
# ]


urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/album_id/
    #(? P<album_id> isrepresenting 712 as a one word and we can use album_id to save a id), 0-9 is a range for id's
   # url(r'^(?P<album_id>[0-9]+)/$', views.IndexView.as_view, name='detail'),

    # url without view,just an action, pk is primary key.
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]