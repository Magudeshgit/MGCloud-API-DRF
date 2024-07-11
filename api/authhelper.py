
from django.core.exceptions import ObjectDoesNotExist
from .models import Users
from django.utils import timezone

def authenticate(session_id):
        try:
            user = Users.objects.get(session_id=session_id)
            if user.expiration <= timezone.now():
                return user
            else:
                return False
        except ObjectDoesNotExist:
            return False