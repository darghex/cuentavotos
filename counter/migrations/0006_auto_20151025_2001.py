# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0005_auto_20151023_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcaldia',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='concejo',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='gobernacion',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='jal',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
