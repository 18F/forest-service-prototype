from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .forms import PermitForm
from .models import Permit
import logging

# Create your views here.
logger = logging.getLogger(__name__)


def submit(request):
    form = PermitForm(request.POST or None)
    if form.is_valid():
        permit = form.save()
        # send_report_notification(request, permit)
        return redirect(submitted_permit, permit_id = 2)
    return render(request, "specialuseform/submit.html", {'form': form})

def submitted_permit(request, permit_id):
    # logger.error(permit_id)
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    # permit_dict = model_to_dict(permit)
    permit_dict = PermitForm(data=model_to_dict(permit))
    return render(request, "specialuseform/submitted_permit.html", {'permit': permit, 'permit_dict': permit_dict})

# @todo: Fix redirect so users don't get stuck in admin screen. See #7.
@login_required(login_url='/admin/')
def applications(request):
    permits = Permit.objects.all()
    return render(request, "specialuseform/applications.html", {
        'permits': permits
        })
