# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_pend_bookno'),
    ]

    operations = [
        migrations.AddField(
            model_name='pend',
            name='categ',
            field=models.CharField(max_length=30, default='Personal Guest', choices=[('Personal Guest', 'Personal Guest'), ('Departmental Guest', 'Department Guest')]),
        ),
        migrations.AddField(
            model_name='pend',
            name='email',
            field=models.EmailField(max_length=200, default='user@example.com'),
        ),
        migrations.AddField(
            model_name='pend',
            name='expad',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pend',
            name='expdd',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='pend',
            name='purpose',
            field=models.TextField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='pend',
            name='roomsno',
            field=models.CharField(max_length=5, default='1/0'),
        ),
    ]
