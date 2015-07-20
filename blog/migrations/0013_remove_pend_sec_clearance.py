# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_pend_sec_clearance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pend',
            name='sec_clearance',
        ),
    ]
