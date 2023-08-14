from django.urls import path
from .views import *


urlpatterns = [
    path('', showblog, name='showblog'),
    path('<int:post_id>', specific_post, name='specific_post'),
]
