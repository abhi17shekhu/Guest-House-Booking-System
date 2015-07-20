# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150712_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pend',
            name='address',
            field=models.CharField(default='e.g House Number,Street,City,State,PINCODE', max_length=200),
        ),
        migrations.AlterField(
            model_name='pend',
            name='purpose',
            field=models.CharField(default='', max_length=100),
        ),
    ]
