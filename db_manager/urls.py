from django.urls import path
from db_manager import views

urlpatterns = [
    path("", views.home, name="home"),
]
