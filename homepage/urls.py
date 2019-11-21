from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Index , name = "Index"),
    path("contact/" , views.Contact , name = "contact")

]
