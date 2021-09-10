from django.db import models




class Artist(models.Model):
  name = models.CharField('Nom',max_length=200,  unique=True)
  class Meta:
    verbose_name= "Aritste"



class Contact(models.Model):
  email = models.EmailField('email', max_length=200)
  name = models.CharField('Nom', max_length=200)
  class Meta:
    verbose_name= "Prospect"



class  Album(models.Model):
  reference = models.IntegerField('Réference', null=True)
  created_at = models.DateTimeField('date de création', auto_now_add=True)
  available = models.BooleanField('disponible',default=True)
  title = models.CharField('Titre',max_length=200)
  picture = models.ImageField("chemin d'image",upload_to='store/static/store/img')
  artists = models.ManyToManyField(Artist,related_name="album",blank=True)
  class Meta:
    verbose_name= "Disque"



class  Booking(models.Model):
  created_at = models.DateTimeField("date d'envoie",auto_now_add=True)
  contacted = models.BooleanField("Demande traité?",default=False)
  album = models.OneToOneField(Album,on_delete=models.CASCADE )
  contact = models.ForeignKey(Contact, on_delete=models.CASCADE )
  class Meta:
    verbose_name= "Réservation"





