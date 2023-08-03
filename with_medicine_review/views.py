from django.shortcuts import render

# Create your views here.
def review_read(request):
    return render(request, 'review_read.html')