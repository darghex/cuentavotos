# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0004_puesto_zona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcaldia',
            name='observaciones',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asamblea',
            name='observaciones',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='concejo',
            name='observaciones',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gobernacion',
            name='observaciones',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jal',
            name='observaciones',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='votosalcaldia',
            name='votos',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='votosasamblea',
            name='votos',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='votosconcejo',
            name='votos',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='votosgobernacion',
            name='votos',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='votosjal',
            name='votos',
            field=models.SmallIntegerField(null=True, blank=True),
        ),
    ]
