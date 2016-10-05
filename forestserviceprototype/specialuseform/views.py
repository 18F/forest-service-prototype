from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core.mail import send_mail
from .forms import PermitForm
from .models import Permit
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def submit(request, permit_id=None, template_name='specialuseform/submit.html'):
    if permit_id:
        permit = get_object_or_404(Permit, permit_id=permit_id)
        submit_button_text = 'Save Changes'
        send_submitted_email = True
    else:
        permit = Permit()
        submit_button_text = 'Submit Your Application'
        send_submitted_email = False

    form = PermitForm(request.POST or None, instance=permit)
    if request.POST and form.is_valid():
        form.save()
        permit = form.cleaned_data
        permit_url = request.build_absolute_uri(
                                      post.get_absolute_url())
        subject = '{} - Application #{} Has Been Submitted "{}"'.format(permit.event_name, permit.permit_id)
        message = 'Your Application for {} [Application ID#{}] has been recieved.\n\n You will recieved notification via email when your application has been reviewd. \n You may review your status at {}'.format(permit.event_name, permit.permit_id, permit_url)
        send_mail(subject, message, 'admin@myblog.com', permit.email)
        sent = True

        # Save was successful, so redirect to another page
        return redirect(submitted_permit, form.instance.permit_id)

    return render(request, template_name, {
        'form': form, 'submit_text': submit_button_text
    })

def submitted_permit(request, permit_id, check_status=False):
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit_dict = PermitForm(data=model_to_dict(permit))
    return render(request, "specialuseform/submitted_permit.html", {'permit': permit, 'permit_dict': permit_dict})

def cancel(request, permit_id):
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit.status = 'user_cancelled'
    permit.save()
    return render(request, 'specialuseform/cancel_permit.html', {'permit': permit})


# @todo: Fix redirect so users don't get stuck in admin screen. See #7.
@login_required(login_url='/admin/')
def applications(request):
    permits = Permit.objects.all().order_by('-status', 'start_date', 'created')
    return render(request, "specialuseform/applications.html", {
        'permits': permits
        })
