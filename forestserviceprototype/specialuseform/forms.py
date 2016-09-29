
from localflavor.us import forms as localflavor
from .models import Permit
import floppyforms.__future__ as forms
from form_utils.forms import BetterModelForm

class PermitForm(BetterModelForm):
    class Meta:
        model = Permit
        fieldsets = [
        ('general', {
                'fields': ['event_name', 'organizer_address_1', 'organizer_address_2', 'city', 'state', 'zipcode', 'email', 'phone_daytime', 'phone_evening'],
                'legend': 'Organizer Information',
            }),
        ('event_details', {
                'fields': ['description', 'location', 'participant_number', 'spectator_number', 'start_date', 'end_date'],
                'legend': 'Event Details',
            }),
        ('primary_permit_holder', {
                'fields': ['permit_holder_name', 'permit_holder_address_1', 'permit_holder_address_2', 'permit_holder_city', 'permit_holder_state', 'permit_holder_zipcode', 'permit_holder_signature'],
                'legend': 'Primary Permit Holder Information',
                'classes': ['permit_holder_1_fieldset']
            }),
        ('secondary_permit_holder', {
                'fields': ['permit_holder_2_name', 'permit_holder_2_address_1', 'permit_holder_2_address_2', 'permit_holder_2_city', 'permit_holder_2_state', 'permit_holder_2_zipcode', 'permit_holder_2_signature'],
                'legend': 'Secondary Permit Holder Information',
                'classes': ['permit_holder_fieldset', 'permit_hide']
            }),
        ]
        widgets = {
            'city': forms.TextInput(attrs={'class': 'medium-grid'}),
            'state': forms.Select(attrs={'class': 'small-grid'}),
            'zipcode': forms.TextInput(attrs={'class': 'usa-input-medium'}),
            'phone_daytime': forms.PhoneNumberInput(attrs={'class': 'medium-grid'}),
            'phone_evening': forms.PhoneNumberInput(attrs={'class': 'medium-grid'}),
            'start_date': forms.DateInput(attrs={'class': 'medium-grid'}),
            'end_date': forms.DateInput(attrs={'class': 'medium-grid'}),
            'permit_holder_city': forms.TextInput(attrs={'class': 'medium-grid'}),
            'permit_holder_state': forms.Select(attrs={'class': 'small-grid'}),
            'permit_holder_zipcode': forms.TextInput(attrs={'class': 'usa-input-medium'}),
            'permit_holder_2_city': forms.TextInput(attrs={'class': 'medium-grid'}),
            'permit_holder_2_state': forms.Select(attrs={'class': 'small-grid'}),
            'permit_holder_2_zipcode': forms.TextInput(attrs={'class': 'usa-input-medium'}),
        }
