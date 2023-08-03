from django.shortcuts import render

# Create your views here.
def free_read(request):
    return render(request, 'free_read.html')