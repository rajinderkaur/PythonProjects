from django.shortcuts import render
from django.views import generic
from .models import Album
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
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


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    #used to represent the object
    context_object_name = 'all_albums'

#querying the database to get all the albums
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    # this means which table details we need to display
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    #what kind of object you need to save in DB, in this case it is album
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    #what kind of object you need to update in DB, in this case it is album
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    #what kind of object you need to delete in DB, in this case it is album
    model = Album
    # after delete where to redirect
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

#if your method is get in form, use this, blank form
    def get(self, request):
        form = self.form_class(None)
        #returning a blank form
        return render(request, self.template_name, {'form': form})

    # process form data if the method is post
    def post(self, request):
        form = self.form_class(request.POST)


#validating the form before saving it to the database
        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized the data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #if u need to change the password
            user.set_password(password)
            user.save()

            #Authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

                #if user could not login , he will redirect to this form
                return render(request, self.template_name, {'form': form})
