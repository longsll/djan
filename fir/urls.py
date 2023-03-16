from django.urls import path
from fir.views import index

urlpatterns = [
    path("",index, name="index"),
]
