from django.urls import path
from . import views

urlpatterns = [
    path('',views.viewindex,name='index' ),
    path('main/',views.viewMain,name='main' ),
    
]