import json

from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Patient


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


@csrf_exempt  # hack to quickly get this to work without session cookie
def get_all_patients(request: HttpRequest):
    if request.method == 'GET':
        return JsonResponse({"Patients": list(Patient.objects.all().values())})
    if request.method == 'POST':
        body = json.loads(request.body)
        p = Patient(patient_first_name=body["patient_first_name"],
                    patient_last_name=body["patient_last_name"],
                    patient_birthdate=body["patient_birth_date"])
        p.save()
        return HttpResponse("All Good")
