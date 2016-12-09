import pytest
from specialuseform import views


def test_home(rf):
    request = rf.get('/')
    response = views.home(request)
    assert response.status_code == 200


def test_submit_view(rf):
    request = rf.get('/submit')
    response = views.submit(request)
    assert response.status_code == 200
