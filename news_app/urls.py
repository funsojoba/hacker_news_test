from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('details/<str:id>', details, name="details"),
    path('create/', create_post, name="create"),
    path('search/', news_search, name='news_search'),
    path('update/<str:id>/', news_update, name='update'),
]

