from rest_framework.response import Response
from rest_framework import status
from .models import Hopitals,article
from .serializers import hospitalsSerializers,ArticleSerial
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from django.conf import settings
import googlemaps
from rest_framework.permissions import AllowAny
class AddingArticle(CreateAPIView):
    queryset = article.objects.all()
    serializer_class = ArticleSerial
    permission_classes = (AllowAny,)
class Getarticle(APIView):
    def get(self,requeest):
        articles=article.objects.all() 
        serial=ArticleSerial(articles,many=True)
        return Response(serial.data, status=status.HTTP_200_OK )  


class UnseulHopital(APIView):

    def get(self,request,id):
        try:
            hospital = Hopitals.objects.get(id=id)
            serial = hospitalsSerializers(hospital)
        except:
            message={"msg":"id inexitant"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)

        return Response(serial.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            hospital = Hopitals.objects.get(id=id)
            serial = hospitalsSerializers(hospital)
        except:
            message = {"msg": "id inexitant"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            hoptal=Hopitals.objects.get(id=id)
        except Hopitals.DoesNotExist:
            messagee={"message":"cet hopital n'exite pas"}
            return Response(messagee,status=status.HTTP_400_BAD_REQUEST)
        hoptal.delete()
        messagee={"message":"cet hopital a été effacé"}
        return Response(messagee,status=status.HTTP_204_NO_CONTENT)
        
class touslesHopital(APIView):

    def get(self, request):
        hospitals = Hopitals.objects.all()
        serial = hospitalsSerializers(hospitals, many=True)
        return Response(serial.data)

    def post(self, request):
        serializer = hospitalsSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getNearHospital(request,lat,lng):
    api_key=settings.GOOGLE_API_KEY
    client_go = googlemaps.Client(api_key)
    lati=float(lat)

    lngi=float(lng)
    try:
        search_string = "hospital"
        distance = 1000
        result = client_go.places_nearby(
                location=(lati,lngi),
                keyword=search_string,
                radius=distance)
       # list=[]
        #for i in result:
         #   listho=[i['']]



        return Response(result.get('results'))
    except: 
        message={"location":"not found"}
        return (message)