import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from .models import Patient


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def get_all_patients(request):
    return JsonResponse({"Patients": list(Patient.objects.all().values())})
