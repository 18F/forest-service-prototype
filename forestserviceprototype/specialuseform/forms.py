
from localflavor.us import forms as localflavor
from .models import Permit
import floppyforms.__future__ as forms
from form_utils.forms import BetterModelForm


class PermitForm(BetterModelForm):
    class Meta:
        model = Permit
        fieldsets = [
            ('general', {
                'fields': [
                    'event_name', 'applicant_address_1',
                    'applicant_address_2', 'applicant_city',
                    'applicant_state', 'applicant_zipcode', 'applicant_email',
                    'applicant_phone_daytime', 'applicant_phone_evening'],
                'legend': 'Applicant Information',
            }),
            ('event_details', {
                'fields': [
                    'description', 'location', 'participant_number',
                    'spectator_number', 'start_date', 'end_date'],
                'legend': 'Event Details',
            }),
            ('primary_permit_holder', {
                'fields': [
                    'permit_holder_name', 'permit_holder_address_1',
                    'permit_holder_address_2', 'permit_holder_city',
                    'permit_holder_state', 'permit_holder_zipcode',
                    'permit_holder_signature'],
                'legend': 'Primary Permit Holder Information',
                'classes': ['permit_holder_1_fieldset']
            }),
            ('secondary_permit_holder', {
                'fields': [
                    'permit_holder_2_name', 'permit_holder_2_address_1',
                    'permit_holder_2_address_2', 'permit_holder_2_city',
                    'permit_holder_2_state', 'permit_holder_2_zipcode',
                    'permit_holder_2_signature'],
                'legend': 'Secondary Permit Holder Information',
                'classes': ['permit_holder_fieldset', 'permit_hide']
            }),
        ]
        widgets = {
            'zipcode': forms.TextInput(attrs={
                'class': 'usa-input-medium',
                'max_length': 5,
                'min_length': 5
            }),
            'start_date': forms.DateInput(),
            'end_date': forms.DateInput(),
            'permit_holder_zipcode': forms.TextInput(attrs={
                'class': 'usa-input-medium'
            }),
            'permit_holder_2_zipcode': forms.TextInput(attrs={
                'class': 'usa-input-medium'
            }),
        }
