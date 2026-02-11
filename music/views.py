from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from music.forms import ArtistForm, AlbumForm, SongsForm
from music.models import Artist, Album, Songs


def index(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'music/index.html', context)


def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return JsonResponse({'success': True, 'message': f'Artista "{artist.name}" creado correctamente'})
    return JsonResponse({'success': False, 'message': 'Error al crear artista'})


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_detail', artist_id=artist.id)
    else:
        form = ArtistForm(instance=artist)
    context = {'artist': artist, 'form': form}
    return render(request, 'music/artist_detail.html', context)


def artist_delete(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        artist.delete()
        return redirect('index')
    context = {'artist': artist}
    return render(request, 'music/artist_delete_confirm.html', context)


def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return JsonResponse({'success': True, 'message': f'Álbum "{album.name}" creado correctamente'})
    return JsonResponse({'success': False, 'message': 'Error al crear álbum'})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    context = {'album': album, 'form': form}
    return render(request, 'music/album_detail.html', context)


def album_delete(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    artist_id = album.artist.id
    if request.method == 'POST':
        album.delete()
        return redirect('artist_detail', artist_id=artist_id)
    context = {'album': album}
    return render(request, 'music/album_delete_confirm.html', context)


def song_create(request):
    if request.method == 'POST':
        form = SongsForm(request.POST)
        if form.is_valid():
            song = form.save()
            return JsonResponse({'success': True, 'message': f'Canción "{song.name_song}" creada correctamente'})
    return JsonResponse({'success': False, 'message': 'Error al crear canción'})


def song_detail(request, song_id):
    songs = get_object_or_404(Songs, id=song_id)
    if request.method == 'POST':
        form = SongsForm(request.POST, instance=songs)
        if form.is_valid():
            form.save()
            return redirect('song_detail', song_id=songs.id)
    else:
        form = SongsForm(instance=songs)
    context = {'songs': songs, 'form': form}
    return render(request, 'music/song_detail.html', context)


def song_delete(request, song_id):
    song = get_object_or_404(Songs, id=song_id)
    album_id = song.album.id
    if request.method == 'POST':
        song.delete()
        return redirect('album_detail', album_id=album_id)
    context = {'song': song}
    return render(request, 'music/song_delete_confirm.html', context)
