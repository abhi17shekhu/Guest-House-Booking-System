# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_pend_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='pend',
            name='tele_no',
            field=models.CharField(max_length=20, default='CountryCode-Number'),
        ),
    ]
