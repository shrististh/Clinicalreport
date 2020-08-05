from django.shortcuts import render,redirect
# from patient.models import Patient
# from patient.models import Patient
# from patient.forms import PatientForm
# Create your views here.


def login(request):
    return render(request,"login/login.html")
    