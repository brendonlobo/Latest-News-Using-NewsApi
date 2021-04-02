from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('entertainment/',views.entertainment,name="entertainment"),
    path('sports/',views.sports,name="sports"),
    path('technology/',views.technology,name="technology"),
]
