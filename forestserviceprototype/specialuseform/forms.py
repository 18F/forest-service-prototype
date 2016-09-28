
from localflavor.us import forms as localflavor
from .models import Permit
import floppyforms.__future__ as forms
from form_utils.forms import BetterForm

class PermitForm(BetterForm):
    class Meta:
        model = Permit
        # fields = ['event_name', 'organizer_address_1', 'organizer_address_2', 'city', 'state', 'zipcode', 'email', 'phone_daytime', 'phone_evening', 'description', 'location', 'participant_number', 'spectator_number', 'start_date', 'end_date', 'permit_holder_name', 'permit_holder_signature']
        fieldsets = [
        ('test', {
                'fields': ['event_name', 'organizer_address_1'],
                'legend': 'a test legend',
            })
        ]
        widgets = {
            'phone_daytime': forms.PhoneNumberInput,
            'phone_evening': forms.PhoneNumberInput
        }
