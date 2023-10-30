from django.urls import path
from . import views

urlpatterns = [
    path("get-mobiles",views.get_mobiles,name="get_mobiles")
]