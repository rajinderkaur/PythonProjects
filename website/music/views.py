from django.shortcuts import render
from django.views import generic
from .models import Album
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

#please check the commented code too


#Please check the commented code- it was used to display the views before we star

#
# # Create your views here.
# # in index view, we are showing the view page using album id.
# def index(request):
#     all_albums = Album.objects.all()
#        # context is a dictionary and use to send value from view to templates
#     context = {'all_albums': all_albums}
#     # render has built in httpresponse
#     return render(request,'music/index.html',context)
#
#
# # use 404 object instead of try except block
# def detail(request, album_id):
#     all_albums = Album.objects.all()
#     album = get_object_or_404(Album, pk=album_id)
#
#     context = {'all_albums': all_albums,
#                    'album': album}
#     return render(request,'music/detail.html', context)
#
#
# #old way of doing using try except
# def detail_copy(request, album_id):
#     all_albums = Album.objects.all()
#
#     # if album id does not exist then send http404 not found error
#     try:
#         album = Album.objects.get(id=album_id)
#         context = {'all_albums': all_albums,
#                    'album': album}
#     except Album.DoesNotExist:
#         raise Http404("Album does not exist")
#     return render(request,'music/detail.html', context)
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, Song.DoestNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': "You did not select a valid song",
#
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})




