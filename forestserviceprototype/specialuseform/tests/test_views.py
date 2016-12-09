import pytest
from django.contrib.auth.models import AnonymousUser
from specialuseform import views
from specialuseform.factories import PermitFactory


def test_home(rf):
    request = rf.get('/')
    response = views.home(request)
    assert response.status_code == 200


def test_submit_view(rf):
    request = rf.get('/submit')
    response = views.submit(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_view(rf):
    permit = PermitFactory()
    request = rf.get('/submit/'+str(permit.permit_id))
    response = views.submit(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_change_status(rf):
    permit = PermitFactory()
    request = rf.post(
        '/change/'+str(permit.permit_id)+'/approved/',
        {'deny_reason': 'dunno'}
    )
    response = views.change_application_status(
        request,
        permit_id=permit.permit_id,
        status='approved'
    )
    assert response.status_code == 200


def test_lacks_perm(rf):
    request = rf.get('/applications/')
    request.user = AnonymousUser()
    response = views.applications(request)
    assert response.status_code == 302
