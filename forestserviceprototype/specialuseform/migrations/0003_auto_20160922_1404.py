# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-22 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialuseform', '0002_auto_20160921_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='status',
            field=models.CharField(choices=[('needs_approval', 'Needs Approval'), ('approved', 'Approved'), ('in_review', 'In Review'), ('not_approved', 'Not Approved')], default='needs_approval', max_length=100),
        ),
    ]