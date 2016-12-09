from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PermitForm
from .models import Permit
from django.forms.models import model_to_dict
from django.core.mail import send_mail, mail_admins
from .forms import PermitForm
from .models import Permit
import logging
import json

# Create your views here.


def home(request):
    return render(request, "specialuseform/home.html")


def submit(request, permit_id=None,
           template_name='specialuseform/submit.html'):
    if permit_id:
        permit = get_object_or_404(Permit, permit_id=permit_id)
        submit_button_text = 'Save Changes'
    else:
        permit = Permit()
        submit_button_text = 'Submit Your Application'

    form = PermitForm(request.POST or None, instance=permit)
    if request.POST and form.is_valid():
        # Save the data to the database
        form.save()

        # Send the user a confirmation message
        send_mail(
            subject='Application Submitted',
            message='Your application for {0} has been received, and is #{1}. '
            'To view its status or make changes, please visit forest-service-'
            'prototype.fr.cloud.gov/submitted/{1}'.format(
                form.instance.event_name,
                form.instance.permit_id,
            ),
            from_email='no-reply@18f.gov',
            recipient_list=[form.instance.email],
            fail_silently=False
        )

        # Send the admins an email about the new permit
        # TODO: The recipient(s) will vary based on the specific forest, but we
        # don't have access to that information until this integrates with SUDS
        send_mail(
            subject='New application',
            message='There\'s a new application for {0}. To see more, and'
            'approve or reject it, please visit forest-service-'
            'prototype.fr.cloud.gov/submitted/{1}'.format(
                form.instance.event_name,
                form.instance.permit_id,
            ),
            from_email='no-reply@18f.gov',
            recipient_list=[],
            fail_silently=False
        )

        # Save was successful, so redirect to another page
        return redirect('/submitted/'+str(form.instance.permit_id)+'?new=true')

    return render(request, template_name, {
        'form': form, 'submit_text': submit_button_text
    })


def submitted_permit(request, permit_id):
    check_status = False if request.GET.get('new') else True
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit_dict = PermitForm(data=model_to_dict(permit))
    return render(request,
                  "specialuseform/submitted_permit.html",
                  {'permit': permit,
                   'permit_dict': permit_dict,
                   'check_status': check_status
                   }
                  )


def change_application_status(request, permit_id, status):
    decision_explanation = request.POST.get('deny_reason')
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit.decision_explanation = decision_explanation
    permit.status = status
    permit.save()

    # Send an email notification with the status update
    send_mail(
        subject='Application Status Changed',
        message='The status for your application for %s has been updated to %s. \
        For more information, please visit forest-service-\
        prototype.fr.cloud.gov/submitted/%s'.format(
            permit.event_name,
            permit.status,
            permit.permit_id
        ),
        from_email='no-reply@18f.gov',
        recipient_list=[permit.email],
        fail_silently=False
    )

    json_response = json.dumps(
        {"status": permit.status, "reason": permit.decision_explanation}
    )

    return HttpResponse(json_response, content_type="application/json")


def cancel(request, permit_id):
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    permit.status = 'user_cancelled'
    permit.save()
    return render(request, 'specialuseform/cancel_permit.html',
                  {'permit': permit})


def print_permit(request, permit_id):
    permit = get_object_or_404(Permit.objects.filter(permit_id=permit_id))
    return render(request, 'specialuseform/print_permit.html',
                  {'permit': permit})


# @todo: Fix redirect so users don't get stuck in admin screen. See #7.
@login_required(login_url='/admin/')
def applications(request):
    permits = Permit.objects.all().order_by('-status', 'start_date', 'created')
    return render(request, "specialuseform/applications.html", {
        'permits': permits
        })
