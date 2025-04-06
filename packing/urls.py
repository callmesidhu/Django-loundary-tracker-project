from django.urls import path
from . import views
from .views import update_task

urlpatterns = [
    path("", views.packing),
    path('update/', update_task, name='update-task')
]