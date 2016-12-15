import pytest
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from specialuseform import views
from specialuseform.factories import PermitFactory


def test_home(rf):
    request = rf.get('/')
    response = views.home(request)
    assert response.status_code == 200


def test_submit_get(rf):
    request = rf.get('/submit')
    response = views.submit(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_submit_post(rf):
    # permit = PermitFactory()
    from django.core import mail
    request = rf.post('/submit/', data={
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
        'start_date': '2016-12-12',
        'end_date': '2016-12-12',
        'permit_holder_name': 'I. M. User',
        'permit_holder_address_1': '456 User Avenue',
        'permit_holder_city': 'Testville',
        'permit_holder_state': 'CO',
        'permit_holder_zipcode': 54321,
        'email': 'user@notawebsite.gov'
    })
    response = views.submit(request)
    assert len(mail.outbox) == 1
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_view(rf):
    permit = PermitFactory()
    request = rf.get('/submit/'+str(permit.id))
    response = views.submit(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_status(rf):
    permit = PermitFactory()
    request = rf.post(
        '/change/'+str(permit.id)+'/approved/',
        {'deny_reason': 'dunno'}
    )
    response = views.change_application_status(
        request,
        id=permit.id,
        status='approved'
    )
    assert response.status_code == 200


def test_lacks_perm(rf):
    request = rf.get('/applications/')
    request.user = AnonymousUser()
    response = views.applications(request)
    assert response.status_code == 302
