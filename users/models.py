from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField
from django.db import models

# from deadline.models import Department

class User(AbstractUser):
    """
    Default custom user model for Ho.uz.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField("Name of User", blank=True, max_length=255)
    avatar = ImageField(blank=True, null=True, upload_to="avatars/")
    # department = models.ForeignKey(Department,on_delete=models.CASCADE, null=True, blank=True)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

