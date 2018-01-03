import pytest

from django.contrib.auth.models import User
# allow all tests in this modules databasea access
pytestmark = pytest.mark.django_db

def test_with_db_access_1():
    pass

def test_with_db_access_2():
    pass

def test_with_db_access_3():
    pass

def test_user_count():
    assert User.objects.count() == 0

