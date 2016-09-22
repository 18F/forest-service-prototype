from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PermitForm
from .models import Permit

# Create your views here.

def submit(request):
    form = PermitForm(request.POST or None)
    if form.is_valid():
        permit = form.save()
        # send_report_notification(request, permit)
        return redirect(submitted_permit)
    return render(request, "specialuseform/submit.html", {'form': form})

def submitted_permit(request):
    return render(request, "specialuseform/submitted_permit.html")

def applications(request):
    permits = Permit.objects.all()
    return render(request, "specialuseform/applications.html", {
        'permits': permits
        })