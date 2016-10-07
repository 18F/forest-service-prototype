from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .forms import PermitForm
from .models import Permit
import logging
import json

# Create your views here.
logger = logging.getLogger(__name__)

def home(request):
    return render(request, "specialuseform/home.html")

def submit(request, permit_id=None, template_name='specialuseform/submit.html'):
    if permit_id:
        permit = get_object_or_404(Permit, permit_id=permit_id)
        submit_button_text = 'Save Changes'
    else:
        permit = Permit()
        submit_button_text = 'Submit Your Application'

    form = PermitForm(request.POST or None, instance=permit)
    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        return redirect('/submitted/'+str(form.instance.permit_id)+'?new=true')

    return render(request, template_name, {
        'form': form, 'submit_text': submit_button_text
    })

def submitted_permit(request, permit_id):
    check_status = False if request.GET.get('new') else True
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit_dict = PermitForm(data=model_to_dict(permit))
    return render(request, "specialuseform/submitted_permit.html", {'permit': permit, 'permit_dict': permit_dict, 'check_status': check_status})

def change_application_status(request, permit_id, status):
    decision_explanation = request.POST.get('deny_reason')
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit.decision_explanation = decision_explanation
    permit.status = status
    permit.save()
    # @TODO: Add email notification to permit.email that application status has changed
    return HttpResponse( json.dumps({"status": permit.status, "reason": permit.decision_explanation}),
            content_type="application/json"
        )

def cancel(request, permit_id):
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit.status = 'user_cancelled'
    permit.save()
    return render(request, 'specialuseform/cancel_permit.html', {'permit': permit})

def print_permit(request, permit_id):
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    return render(request, 'specialuseform/print_permit.html', {'permit': permit})

# @todo: Fix redirect so users don't get stuck in admin screen. See #7.
@login_required(login_url='/admin/')
def applications(request):
    permits = Permit.objects.all().order_by('-status', 'start_date', 'created')
    return render(request, "specialuseform/applications.html", {
        'permits': permits
        })
