# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
