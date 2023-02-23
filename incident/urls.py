from django.urls import path
from .views import *

urlpatterns = [
    path('signup/',SignUpUserView.as_view(),name='UserSignup'),
    path('login/',LoginUserView.as_view(),name='UserLogin'),
    path('getuser/',GetAllUserView.as_view(),name='GetUser'),
    path('create_incident/',IncidentCreateView.as_view(),name='incident-create-view'),
    path('incident-all-details/',GetAllIncidentDetailsView.as_view(),name='incident-all-details')
]

