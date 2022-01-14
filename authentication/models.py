from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        null=True
    )
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=15, unique=True, null=True)  # FIXME: Change to INT???
    # type = models.IntegerField()
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=150, null=True)
    is_active = models.BooleanField(default=False)
    user_avatar_directory = models.TextField(null=True)
    register_mode = models.CharField(max_length=25)
    updated_at = models.DateTimeField(null=True)


class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
