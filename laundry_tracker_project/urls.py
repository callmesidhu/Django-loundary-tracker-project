from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("loading-start/", include("loading_start.urls")),
    path("loading-end/", include("loading_end.urls")),
    path("unloading-start/", include("unloading_start.urls")),
    path("unloading-end/", include("unloading_end.urls")),
    path("nursing-station/", include("nursing_station.urls")),
    path("task-schedule/", include("task_schedule.urls")),
    path("packing/", include("packing.urls")),
    path("accounts/", include("accounts.urls")),
]