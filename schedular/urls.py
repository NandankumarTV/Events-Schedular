from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('chooseLocationEdu',views.chooseLocationEdu),
    path('chooseLocationSpo',views.chooseLocationSpo),
    path('chooseLocationCha',views.chooseLocationCha),
    path('chooseLocationCul',views.chooseLocationCul),
    path('EduBang',views.EduBang),
    path('EduChen',views.EduChen),
    path('EduMumb',views.EduMumb),
    path('EduKol',views.EduKol),
    path('EduAny',views.EduAny),
    path('SpoBang',views.SpoBang),
    path('SpoChen',views.SpoChen),
    path('SpoMumb',views.SpoMumb),
    path('SpoKol',views.SpoKol),
    path('SpoAny',views.SpoAny),
    path('ChaBang',views.ChaBang),
    path('ChaChen',views.ChaChen),
    path('ChaMumb',views.ChaMumb),
    path('ChaKol',views.ChaKol),
    path('ChaAny',views.ChaAny),
    path('CulBang',views.CulBang),
    path('CulChen',views.CulChen),
    path('CulMumb',views.CulMumb),
    path('CulKol',views.CulKol),
    path('CulAny',views.CulAny),
    path('EduBangDetails1',views.EduBangDetails1),
    path('EduBangDetails2',views.EduBangDetails2),
    path('EduChenDetails1',views.EduChenDetails1),
    path('EduChenDetails2',views.EduChenDetails2),  
    path('EduKolDetails',views.EduKolDetails),  
    path('EduMumbDetails',views.EduMumbDetails),  
    path('SpoBangDetails1',views.SpoBangDetails1),
    path('SpoBangDetails2',views.SpoBangDetails2),
    path('SpoChenDetails1',views.SpoChenDetails1),
    path('SpoChenDetails2',views.SpoChenDetails2),  
    path('SpoKolDetails',views.SpoKolDetails),  
    path('SpoMumbDetails',views.SpoMumbDetails),   
    path('ChaBangDetails1',views.ChaBangDetails1),
    path('ChaBangDetails2',views.ChaBangDetails2),    
    path('ChaKolDetails',views.ChaKolDetails), 
    path('ChaChenDetails',views.ChaChenDetails),
    path('ChaMumbDetails1',views.ChaMumbDetails1),
    path('ChaMumbDetails2',views.ChaMumbDetails2),
    path('CulBangDetails1',views.CulBangDetails1),
    path('CulBangDetails2',views.CulBangDetails2),
    path('CulChenDetails',views.CulChenDetails),
    path('CulKolDetails1',views.CulKolDetails1),
    path('CulKolDetails2',views.CulKolDetails2),
    path('CulMumbDetails',views.CulMumbDetails),  
]
