# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-29 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('specialuseform', '0008_auto_20160927_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_address_1',
            field=models.CharField(blank=True, max_length=250, verbose_name='Street Address 1'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_address_2',
            field=models.CharField(blank=True, max_length=250, verbose_name='Street Address 2'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_city',
            field=models.CharField(blank=True, max_length=250, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_name',
            field=models.CharField(default='Additional Permit Holder', help_text='Name of Permit Holder', max_length=250),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_signature',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_state',
            field=localflavor.us.models.USStateField(blank=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_2_zipcode',
            field=localflavor.us.models.USZipCodeField(blank=True, verbose_name='Zipcode'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_address_1',
            field=models.CharField(default=1, max_length=250, verbose_name='Street Address 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_address_2',
            field=models.CharField(blank=True, max_length=250, verbose_name='Street Address 2'),
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_city',
            field=models.CharField(default=1, max_length=250, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_state',
            field=localflavor.us.models.USStateField(default=1, verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permit',
            name='permit_holder_zipcode',
            field=localflavor.us.models.USZipCodeField(default='00001', verbose_name='Zipcode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='permit',
            name='participant_number',
            field=models.IntegerField(help_text='This is the number of participants who will partake in the event.', verbose_name='Number of Participants'),
        ),
        migrations.AlterField(
            model_name='permit',
            name='permit_holder_name',
            field=models.CharField(help_text='Name of Permit Holder', max_length=250),
        ),
        migrations.AlterField(
            model_name='permit',
            name='spectator_number',
            field=models.IntegerField(blank=True, help_text='If your event will have spectators (such as at a sporting event), please note how many additional people will be spectators.', verbose_name='Number of Spectators'),
        ),
    ]