from django.urls import path
from . import views

urlpatterns = [
    path("", views.Select_view, name="select"),
]
