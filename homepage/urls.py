from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path("" , views.Index , name = "Index"),
    path("contact/" , views.Contact , name = "contact"),
    path("success/" , views.Success , name = "success"),

]
