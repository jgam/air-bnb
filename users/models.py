# username, firstname, lastname blah blah is AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
import uuid
from . import core

# Create your models here.


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),

    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_KOREAN = 'kr'

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_ENGLISH, "English"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, deafult=LANGUAGE_KOREAN)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW)
    superhost = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)

    def verify_email(self):
        if self.email_email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            send_mail("Verify Airbnb account", 
                        f"Verify account, this is ur secret: {secret}", 
                        core.settings.EMAIL_FROM,
                        [self.email], fail_silently=False)
        return
