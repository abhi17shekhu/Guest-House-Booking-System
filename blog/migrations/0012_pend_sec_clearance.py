# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pend',
            name='sec_clearance',
            field=models.ForeignKey(null=True, to='blog.UserProfile'),
        ),
    ]
