from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/create/', views.artist_create, name='artist_create'),
    path('artist/<int:artist_id>', views.artist_detail, name='artist_detail'),
    path('artist/<int:artist_id>/delete/', views.artist_delete, name='artist_delete'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/<int:album_id>', views.album_detail, name='album_detail'),
    path('album/<int:album_id>/delete/', views.album_delete, name='album_delete'),
    path('song/create/', views.song_create, name='song_create'),
    path('song/<int:song_id>', views.song_detail, name='song_detail'),
    path('song/<int:song_id>/delete/', views.song_delete, name='song_delete'),
]
