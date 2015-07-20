# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_pend_gname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pend',
            name='dept',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='pend',
            name='status',
            field=models.TextField(default='Pending'),
        ),
    ]
