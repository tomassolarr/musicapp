from django import forms
from music.models import Artist, Album, Songs

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = '__all__'