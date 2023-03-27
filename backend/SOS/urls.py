
from django.urls import path,include
from .views import touslesHopital,UnseulHopital,getNearHospital,AddingArticle,Getarticle

api1="tousleshopitaux/"
api2="unseulHopital/<int:id>/"
apihp="hp/<str:lat>/<str:lng>/"
api4="addarticle/"
api5="getallarticles/"
urlpatterns = [

    path(api1,touslesHopital().as_view()),
    path(api2,UnseulHopital().as_view()),
    path(apihp,getNearHospital),
    path(api4,AddingArticle.as_view()),
    path(api5,Getarticle().as_view())
    ]
