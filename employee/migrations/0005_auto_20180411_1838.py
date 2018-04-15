# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20180411_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id_number',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='physical_address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
