from django.urls import path
from .views import *

app_name = "dr"
urlpatterns = [
    path('', homepage,name="homepage"),
]