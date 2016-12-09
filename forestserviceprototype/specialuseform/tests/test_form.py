import pytest
from django.utils import timezone
from specialuseform.forms import PermitForm


def test_form():
    form_data = {
        'event_name': 'hi',
        'organizer_address_1': '123 Forest Lane',
        'city': 'Treeville',
        'state': 'CO',
        'zipcode': 12345,
        'phone_daytime': '555-555-5555',
        'description': 'wow. such permit. very event.',
        'location': 'a park',
        'participant_number': 1000,
        'spectator_number': 5000,
        'start_date': timezone.now(),
        'end_date': timezone.now(),
        'permit_holder_name': 'I. M. User',
        'permit_holder_address_1': '456 User Avenue',
        'permit_holder_city': 'Testville',
        'permit_holder_state': 'CO',
        'permit_holder_zipcode': 54321,
        'email': 'tester@test.gov'
    }
    form = PermitForm(data=form_data)
    assert form.is_valid()
