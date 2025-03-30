from django.shortcuts import render

# Create your views here.
def packing(request):
        return render(request, "packing.html")