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
        ('not_approved', 'Rejected'),
        ('user_cancelled', 'User Cancelled')
    )
    permit_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=250,
        help_text='The name of the event')
    organizer_address_1 = models.CharField(max_length=250)
    organizer_address_2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250)
    state = localflavor.USStateField()
    zipcode = localflavor.USZipCodeField()
    email = models.EmailField(blank=True)
    phone_daytime = localflavor.PhoneNumberField()
    phone_evening = localflavor.PhoneNumberField(blank=True)
    description = models.TextField()
    location = models.CharField(max_length=250)
    participant_number = models.IntegerField(verbose_name='Number of Participants', help_text='This is the number of people who will directly participate in the event.')
    spectator_number = models.IntegerField(blank=True, verbose_name='Number of Spectators', help_text='If your event will have spectators (such as at a sporting event), please note how many additional people will be spectators.')
    start_date = models.DateTimeField(default=timezone.now, help_text='Format: MM/DD/YYYY')
    end_date = models.DateTimeField(default=timezone.now, help_text='Format: MM/DD/YYYY')
    permit_holder_name = models.CharField(max_length=250, help_text='Name of Permit Holder')
    permit_holder_signature = models.ImageField(blank=True)
    permit_holder_address_1 = models.CharField(max_length=250, verbose_name="Street Address 1")
    permit_holder_address_2 = models.CharField(max_length=250, blank=True, verbose_name="Street Address 2")
    permit_holder_city = models.CharField(max_length=250, verbose_name="City")
    permit_holder_state = localflavor.USStateField(verbose_name="State")
    permit_holder_zipcode = localflavor.USZipCodeField(verbose_name="Zipcode")
    permit_holder_2_name = models.CharField(max_length=250, help_text='Name of Permit Holder')
    permit_holder_2_signature = models.ImageField(blank=True)
    permit_holder_2_address_1 = models.CharField(max_length=250, verbose_name="Street Address 1", blank=True)
    permit_holder_2_address_2 = models.CharField(max_length=250, blank=True, verbose_name="Street Address 2")
    permit_holder_2_city = models.CharField(max_length=250, verbose_name="City", blank=True)
    permit_holder_2_state = localflavor.USStateField(verbose_name="State", blank=True)
    permit_holder_2_zipcode = localflavor.USZipCodeField(verbose_name="Zipcode", blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100,
                              choices=STATUS_CHOICES,
                              default='needs_approval')
    decision_explanation = models.TextField(blank=True)

    def __str__(self):
        return self.event_name
