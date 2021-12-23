from django.http.response import JsonResponse
import json

from django.shortcuts import render
from school.models import Faculty, Department
# Create your views here.


def getLocalGov(request, faculty):
    print(faculty)
    f = Faculty.objects.get(name=faculty)
    response = []
    for s in f.departments.all():
        response.append({
            'name': s.name
        })
    return JsonResponse(response, content_type='application/json', safe=False)


def Institutions(request):
    pass
    return render(request, 'school/institutions.html')
