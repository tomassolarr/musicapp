from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre =models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pub_date=models.DateField('fechade publicación')

    def __str__(self):
        return f"{self.artist.name} - {self.name} - ({self.pub_date.year})"

class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name_song = models.CharField(max_length=200)
    duration = models.IntegerField(default=0)
    video = models.URLField(blank=True, null=True)

    def duration_mmss(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes:02d}:{seconds:02d}"

    def __str__(self):
        return f"{self.album.name} - {self.name_song}"