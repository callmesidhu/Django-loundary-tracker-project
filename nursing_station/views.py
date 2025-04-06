from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TaskSchedule

# Create your views here.
def nursing_station(request):
        return render(request, "nursing_station.jinja")

def add_task_schedule(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Extract data from the POSTed JSON
            uuid = data.get("UUID")
            num_clothes = data.get("Number of Clothes")
            cloth_type = data.get("Type of Clothes")
            cloth_state = data.get("State of Clothes")

            # Create a new TaskSchedule record
            task = TaskSchedule.objects.create(
                uuid=uuid,
                num_clothes=num_clothes,
                cloth_type=cloth_type,
                cloth_state=cloth_state
            )
            return JsonResponse({"status": "success", "message": "Task Schedule created."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request."}, status=400)