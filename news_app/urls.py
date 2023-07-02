from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('details/<str:id>', details, name="details")
]

