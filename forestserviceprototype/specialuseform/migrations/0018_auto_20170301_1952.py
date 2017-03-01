# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-01 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('specialuseform', '0017_auto_20161221_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noncommercialusepermit',
            name='permit_holder_2_signature',
        ),
        migrations.RemoveField(
            model_name='noncommercialusepermit',
            name='permit_holder_signature',
        ),
        migrations.AddField(
            model_name='noncommercialusepermit',
            name='permit_holder_signature_initials',
            field=models.CharField(blank=True, max_length=3, verbose_name='Signature initials'),
        ),
        migrations.AlterField(
            model_name='noncommercialusepermit',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Format: MM/DD/YYYY HH:MM', verbose_name='End date and time'),
        ),
        migrations.AlterField(
            model_name='noncommercialusepermit',
            name='event_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='noncommercialusepermit',
            name='participant_number',
            field=models.IntegerField(help_text='This is the number of people who will directly participate in the event.', verbose_name='Number of participants'),
        ),
        migrations.AlterField(
            model_name='noncommercialusepermit',
            name='permit_holder_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='noncommercialusepermit',
            name='spectator_number',
            field=models.IntegerField(blank=True, help_text='If your event will have spectators (such as at a sporting event), please note how many additional people will be spectators', null=True, verbose_name='Number of spectators'),
        ),
        migrations.AlterField(
            model_name='noncommercialusepermit',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Format: MM/DD/YYYY HH:MM', verbose_name='Start date and time'),
        ),
    ]