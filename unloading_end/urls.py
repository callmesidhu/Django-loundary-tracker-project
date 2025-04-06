from django.urls import path
from . import views
from .views import update_task

urlpatterns = [
    path("", views.unloading_end),
    path('update/', update_task, name='update-task')
]