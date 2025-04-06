from django.urls import path
from . import views
from .views import add_task_schedule

urlpatterns = [
    path("", views.nursing_station),
    path('add/', add_task_schedule, name='add_task_schedule'),
]