from django.urls import path
from .views import *

urlpatterns = [
    path("", indexpage, name=""),
    path("datasave/", datasavepage, name="datasave")
]
