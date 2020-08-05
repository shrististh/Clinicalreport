from django.shortcuts import render,redirect
# from patient.models import Patient
from patient.models import Patient
from patient.forms import PatientForm
# Create your views here.


def index(request):
    print("asd")
    patients = Patient.objects.all()
    print(patients)
    return render(request,"patient/index.html",{'patients': patients})

 

def save(request):
    print("print")
    print(request.POST)
    if request.method=="POST":
        print(request.POST)
        form=PatientForm(request.POST)
        form.save()
        return redirect('/patient')
    else:
        form=PatientForm()
    return render(request,"patient/create.html",{'form':form})

 

def update(request,id):
    patients =Patient.objects.get(patient_id=id)
    if request.method=="POST":
        form=PatientForm(request.POST,instance=patients)
        form.save()
        return redirect("/patient")
    else:
        form=PatientForm(instance=patients)
    return render(request,"patient/edit.html",{'form':form})

 

def delete(request,id):
    patients=Patient.objects.get(patient_id=id)
    patients.delete()
    return redirect("/patient")
