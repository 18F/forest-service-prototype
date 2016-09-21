from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from localflavor.us import models as localflavor

# Create your models here.
class Permit(models.Model):
    STATUS_CHOICES = (
        ('needs_approval', 'Needs Approval'),
        ('approved', 'Approved'),
        ('in_review', 'In Review'),
        ('not_approved', 'Not Approved')
    )
    event_name = models.CharField(max_length=250)
    organizer_address_1 = models.CharField(max_length=250)
    organizer_address_2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = localflavor.USStateField(default="OH")
    zipcode = localflavor.USZipCodeField()
    phone_daytime = localflavor.PhoneNumberField()
    phone_evening = localflavor.PhoneNumberField(blank=True)
    description = models.TextField()
    location = models.CharField(max_length=250)
    participant_number = models.IntegerField()
    spectator_number = models.IntegerField(blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    organizer_name = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='needs_approval')

    def __str__(self):
        return self.event_name
