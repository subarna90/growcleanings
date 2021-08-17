from django.urls import path
from . import views

urlpatterns = [
    path('',views.infectioncontrolcleaning, name='infectioncontrolcleaning'),
    
]