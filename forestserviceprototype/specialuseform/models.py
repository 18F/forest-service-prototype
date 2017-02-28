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
        ('not_approved', 'Not Approved'),
        ('user_cancelled', 'User Cancelled'),
    )

    applicant_address_1 = models.CharField(
        max_length=250,
        blank=False,
    )
    applicant_address_2 = models.CharField(
        max_length=250,
        blank=True,
    )
    applicant_city = models.CharField(
        max_length=250,
        blank=False,
    )
    applicant_state = localflavor.USStateField(
        blank=False,
    )
    applicant_zipcode = localflavor.USZipCodeField(
        blank=False,
    )
    applicant_phone_daytime = localflavor.PhoneNumberField(
        blank=False,
    )
    applicant_phone_evening = localflavor.PhoneNumberField(
        blank=True,
    )
    applicant_email = models.EmailField(
        blank=True,
    )
    permit_holder_name = models.CharField(
        max_length=250,
        blank=False,
    )
    permit_holder_address_1 = models.CharField(
        max_length=250,
        verbose_name="Street Address 1",
        blank=False,
    )
    permit_holder_address_2 = models.CharField(
        max_length=250,
        verbose_name="Street Address 2",
        blank=True,
    )
    permit_holder_city = models.CharField(
        max_length=250,
        verbose_name="City",
        blank=False,
    )
    permit_holder_state = localflavor.USStateField(
        verbose_name="State",
        blank=False,
    )
    permit_holder_zipcode = localflavor.USZipCodeField(
        verbose_name="Zipcode",
        blank=False,
    )
    permit_holder_2_name = models.CharField(
        max_length=250,
        help_text='Name of Permit Holder',
        blank=True,
    )
    permit_holder_2_address_1 = models.CharField(
        max_length=250,
        verbose_name="Street Address 1",
        blank=True,
    )
    permit_holder_2_address_2 = models.CharField(
        max_length=250,
        verbose_name="Street Address 2",
        blank=True,
    )
    permit_holder_2_city = models.CharField(
        max_length=250,
        verbose_name="City",
        blank=True,
    )
    permit_holder_2_state = localflavor.USStateField(
        verbose_name="State",
        blank=True,
    )
    permit_holder_2_zipcode = localflavor.USZipCodeField(
        verbose_name="Zipcode",
        blank=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=False,
    )
    updated = models.DateTimeField(
        auto_now=True,
        blank=False,
    )
    permit_status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='needs_approval',
        blank=False,
    )
    decision_explanation = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.event_name

    class Meta:
        abstract = True


class NonCommercialUsePermit(Permit):
    event_name = models.CharField(
        max_length=250,
        blank=False
    )
    description = models.TextField(
        blank=False,
    )
    location = models.CharField(
        max_length=250,
        blank=False,
    )
    start_date = models.DateTimeField(
        default=timezone.now,
        help_text='Format: MM/DD/YYYY',
        blank=False,
    )
    end_date = models.DateTimeField(
        default=timezone.now,
        help_text='Format: MM/DD/YYYY',
        blank=False,
    )
    participant_number = models.IntegerField(
        verbose_name='Number of participants',
        help_text='This is the number of people who will directly participate '
                  'in the event.',
        blank=False,
    )
    spectator_number = models.IntegerField(
        verbose_name='Number of spectators',
        help_text='If your event will have spectators (such as at a sporting '
                  'event), please note how many additional people will be '
                  'spectators',
        blank=True,
        null=True,
    )
