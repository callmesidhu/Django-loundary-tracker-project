from django.urls import path
from . import views
urlpatterns = [
    path("", views.loading_start),
]