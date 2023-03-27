from .models import *
from  rest_framework import serializers

class ArticleSerial(serializers.ModelSerializer):
    class Meta:
        model=article
        fields='__all__'



class hospitalsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Hopitals
        fields=(
            'id',
            'name',
            'sulg',
            'urgence',
            'localisation',
            'description',
            'image',
            'date_ajout',
            'get_google_Map_Cordonnee',
            'get_url_map'
    )
        
