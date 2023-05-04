from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Landing"),
    path('home.html',views.home,name="Homepage"),
    path('crop_.html',views.crop,name="Crop"),
    path('yield_.html',views.yield_,name="Yield"),
    path('predict',views.predict_,name="Predict"),
]