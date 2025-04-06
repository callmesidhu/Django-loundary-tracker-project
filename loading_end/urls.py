from django.urls import path
from . import views
from .views import update_task

urlpatterns = [
    path("", views.loading_end),
    path('update/', update_task, name='update-task')
]