from django.shortcuts import render

def loading_start(request):
    return render(request, "loading_start.html")
