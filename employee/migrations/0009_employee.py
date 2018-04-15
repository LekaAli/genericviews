# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0008_auto_20180411_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_number', models.CharField(max_length=13, null=True, blank=True)),
                ('phone_number', models.CharField(max_length=10, null=True, blank=True)),
                ('physical_address', models.CharField(max_length=200, null=True, blank=True)),
                ('tax_number', models.CharField(max_length=10, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('personal_email', models.EmailField(max_length=254, null=True, blank=True)),
                ('github_user', models.CharField(max_length=30, null=True, blank=True)),
                ('birth_date', models.DateTimeField(null=True, blank=True)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, choices=[('M', 'Male'), ('F', 'Female')])),
                ('race', models.CharField(blank=True, max_length=1, null=True, choices=[('A', 'African'), ('W', 'White'), ('I', 'Indian'), ('C', 'Coloured'), ('O', 'Others')])),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(related_name='employee', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
