from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import validate_email
from django.core.validators import RegexValidator


class Users(models.Model):
    USERTYPECHOICE = (
        ('1', 'Admin'),
        ('2', 'User'),
    )

    username = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True, null=False,blank=False, validators=[validate_email])
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=False)  # validators should be a list
    user_type = models.CharField(max_length=1, choices=USERTYPECHOICE, blank=False, null=False, default='2')
    created_date = models.DateTimeField(default=timezone.now)
