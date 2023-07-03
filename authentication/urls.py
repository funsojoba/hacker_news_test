from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('forgot-password/', forgot_password, name="forgot_password")
]

