from django.shortcuts import render

# Create your views here.
def loading_end(request):
        return render(request, "loading_end.jinja")