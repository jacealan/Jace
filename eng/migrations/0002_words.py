# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=1)),
            ],
        ),
    ]
