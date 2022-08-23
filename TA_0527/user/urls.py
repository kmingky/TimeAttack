from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.join_view, name="join"),
]
