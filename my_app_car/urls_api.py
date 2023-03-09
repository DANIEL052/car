from django.urls import path
from . import views_api
from rest_framework.views import APIView


urlpatterns = [
    path('car', views_api.APICar.as_view()),
]