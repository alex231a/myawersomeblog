from django.urls import path
from .views import *


urlpatterns = [
    path('', showblog, name='showblog'),
]