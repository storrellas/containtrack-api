from django.urls import path
from rest_framework import routers

from .views import *

urlpatterns = [
    path("", HelloWordAPIView.as_view()),
]


urlpatterns = urlpatterns