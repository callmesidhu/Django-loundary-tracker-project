from django.shortcuts import render

# Create your views here.
def task_schedule(request):
        return render(request, "task_schedule.html")