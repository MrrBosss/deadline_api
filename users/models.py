from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ImageField, Model, CASCADE, ForeignKey



class Department(Model):
    name = CharField(max_length=50,null=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class User(AbstractUser):
    """
    Default custom user model for Ho.uz.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField("Name of User", blank=True, max_length=255)
    avatar = ImageField(blank=True, null=True, upload_to="avatars/")
    department = ForeignKey(Department,on_delete=CASCADE, null=True,blank=True)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
     
    