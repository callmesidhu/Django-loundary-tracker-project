from django.shortcuts import render

# Create your views here.
def nursing_station(request):
        return render(request, "nursing_station.jinja")