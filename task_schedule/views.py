import json
from django.shortcuts import render
from nursing_station.models import TaskSchedule  # Absolute import

def task_schedule(request):
    # Initialize an empty dictionary to hold tasks keyed by date
    tasks_data = {}

    # Query all records from the nursing_station_taskschedule table
    schedules = TaskSchedule.objects.all()

    for record in schedules:
        # Format the created_at datetime to get the date string (YYYY-MM-DD) and time string (HH:MM)
        date_str = record.created_at.strftime('%Y-%m-%d')
        time_str = record.created_at.strftime('%H:%M')

        # Create a list of task dictionaries from the record
        tasks = [
            {"task": "Loading A", "status": record.loading_a, "time": time_str},
            {"task": "Unloading A", "status": record.unloading_a, "time": time_str},
            {"task": "Loading B", "status": record.loading_b, "time": time_str},
            {"task": "Unloading B", "status": record.unloading_b, "time": time_str},
            {"task": "Packing",   "status": record.packing,   "time": time_str},
        ]

        # If there are already tasks for the given date, extend the list, otherwise create a new list.
        if date_str in tasks_data:
            tasks_data[date_str].extend(tasks)
        else:
            tasks_data[date_str] = tasks

    # Pass the tasks_data as a JSON string to the template.
    context = {'tasks_data': json.dumps(tasks_data)}
    return render(request, 'task_schedule.jinja', context)
