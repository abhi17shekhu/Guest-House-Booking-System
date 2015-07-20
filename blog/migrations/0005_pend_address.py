# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_pend_roomsno'),
    ]

    operations = [
        migrations.AddField(
            model_name='pend',
            name='address',
            field=models.TextField(max_length=200, default='e.g House Number,Street,City,State,PINCODE'),
        ),
    ]
