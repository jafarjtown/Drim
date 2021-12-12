from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'activities/index.html')


def ClearAll(request):
    request.user.activities.clear()
    return HttpResponse('Done')