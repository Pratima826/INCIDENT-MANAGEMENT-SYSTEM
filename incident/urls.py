from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',SignUpUserView.as_view(),name='UserSignup'),
    path('login/',LoginUserView.as_view(),name='UserLogin'),
    path('getuser/',GetAllUserView.as_view(),name='GetUser'),
]

