# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20180410_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-id'], 'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AddField(
            model_name='employee',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
