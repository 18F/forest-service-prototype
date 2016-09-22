
from localflavor.us import forms as localflavor
from .models import Permit
import floppyforms.__future__ as forms

class PermitForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = ['event_name', 'organizer_address_1', 'organizer_address_2', 'city', 'state', 'zipcode', 'description', 'location', 'participant_number', 'spectator_number', 'start_date', 'end_date', 'organizer_name']
