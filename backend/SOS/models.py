from django.db import models
import PIL
from django.urls import reverse
import folium


from django.conf import settings


class Infos(models.Model):
    cat = (
        ('mat','Maternite'),
        ('sec','Secours'),
        ('sex','Sexualite'),
        ('div','Divers')
    )
    title = models.CharField(max_length=100)
    overview = models.TextField()
    picture = models.ImageField()
    categorie = models.CharField(max_length=10, choices=cat)

    def __str__(self) -> str:
        return self.title


class Hopitals(models.Model):
    name = models.CharField(max_length=100, unique=True)
    """ ===> ici on a besoin de faire entrer une liste
    specialites"""
    sulg=models.SlugField(default="")

    urgence = models.CharField(max_length=10, unique=True)
    localisation = models.CharField(max_length=20)
    description = models.TextField(null=True)
    image=models.ImageField(upload_to="uploadHospital/",blank=True,null=True)
    date_ajout=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('-date_ajout',)
    def get_google_Map_Cordonnee(self):
        import googlemaps

        API_KEY = settings.GOOGLE_API_KEY
        map_client = googlemaps.Client(API_KEY)
        try:

            address = self.localisation
            geocode = map_client.geocode(address=address)
            (lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))
            coords = (lat, lng)
            if lat==None or lng==None:
                return None
            else:
                return  coords
        except:
            return 0

    def get_url_map(self):
        import googlemaps
        API_KEY = settings.GOOGLE_API_KEY
        map_client = googlemaps.Client(API_KEY)
        try:

            address = self.localisation
            geocode = map_client.geocode(address=address)
            (lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))
            coords = (lat, lng)
            url='https://www.google.com/maps/place/?q=place_id:'+map(geocode[0]['place_id'])
            if lat==None or lng==None:
                return None
            else:
                return  url
        except:
            return 0
        
    def __str__(self) -> str:
        return self.name

class article(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=60)
    about=models.TextField()
    image=models.ImageField(blank=True,null=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    price = models.FloatField(default=1.5)
    slug = models.SlugField(max_length=100)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})
class Maladies(models.Model):
    sympt = (

    )
    symptomes = models.CharField(max_length=10, choices=sympt)
    """specialistes = """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name