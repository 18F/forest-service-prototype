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
        ('not_approved', 'Rejected')
    )
    permit_id = models.AutoField(primary_key=True, default=0)
    event_name = models.CharField(max_length=250,
        help_text='The name of the event')
    organizer_address_1 = models.CharField(max_length=250)
    organizer_address_2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = localflavor.USStateField(default="OH")
    zipcode = localflavor.USZipCodeField()
    email = models.EmailField(blank=True)
    phone_daytime = localflavor.PhoneNumberField()
    phone_evening = localflavor.PhoneNumberField(blank=True)
    description = models.TextField()
    location = models.CharField(max_length=250)
    participant_number = models.IntegerField()
    spectator_number = models.IntegerField(blank=True)
    start_date = models.DateTimeField(default=timezone.now, help_text='For example: 04 28 1986')
    end_date = models.DateTimeField(default=timezone.now, help_text='For example: 04 28 1986')
    permit_holder_name = models.CharField(max_length=250, help_text='Name of Permit Holder', default='Permit Holder')
    permit_holder_signature = models.ImageField(blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100,
                              choices=STATUS_CHOICES,
                              default='needs_approval')

    def __str__(self):
        return self.event_name
