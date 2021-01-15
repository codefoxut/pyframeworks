import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_count():
    assert User.objects.count() == 0
