from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from nursing_station.models import TaskSchedule

def unloading_end(request):
    return render(request, "unloading_end.jinja")

def update_task(request):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            uuid = data.get("uuid")
            if not uuid:
                return JsonResponse({"status": "error", "message": "UUID not provided."}, status=400)
            
            # Fetch the record. Adjust field names and filters as necessary.
            task = TaskSchedule.objects.get(uuid=uuid)
            
            # Update only the loading_a field to "Completed"
            task.unloading_b = "Completed"
            task.save()

            return JsonResponse({"status": "success"})
        except TaskSchedule.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Task not found."}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)