import json
from django.shortcuts import render

def task_schedule(request):
    tasks_data = {
    "2025-03-28": [
        {"task": "Washing", "status": "Pending", "time": "08:00"},
        {"task": "Drying", "status": "Pending", "time": "10:00"},
        {"task": "Folding", "status": "Completed", "time": "12:00"}
    ],
    "2025-03-31": [
        {"task": "Review Reports", "status": "Pending", "time": "14:00"}
    ],
    "2025-04-04": [ 
        {"task": "Washing", "status": "Pending", "time": "08:00"},
        {"task": "Drying", "status": "Pending", "time": "10:00"},
        {"task": "Folding", "status": "Completed", "time": "12:00"}
    ],
}

    # Pass tasks_data as a JSON object to the template.
    context = {'tasks_data': json.dumps(tasks_data)}
    return render(request, 'task_schedule.html', context)
