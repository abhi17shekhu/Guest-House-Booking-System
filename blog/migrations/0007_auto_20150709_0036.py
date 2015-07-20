# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_pend_tele_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pend',
            name='status',
            field=models.CharField(max_length=40, default='Pending', choices=[('Pending', 'Pending'), ('Granted', 'Granted'), ('Arrived', 'Arrived'), ('Departed', 'Departed')]),
        ),
    ]
