# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='votosalcaldia',
            options={'ordering': ['candidato__partido', 'candidato__renglon']},
        ),
        migrations.AlterModelOptions(
            name='votosasamblea',
            options={'ordering': ['candidato__partido', 'candidato__renglon']},
        ),
        migrations.AlterModelOptions(
            name='votosconcejo',
            options={'ordering': ['candidato__partido', 'candidato__renglon']},
        ),
        migrations.AlterModelOptions(
            name='votosgobernacion',
            options={'ordering': ['candidato__partido', 'candidato__renglon']},
        ),
        migrations.AlterModelOptions(
            name='votosjal',
            options={'ordering': ['candidato__partido', 'candidato__renglon']},
        ),
        migrations.AddField(
            model_name='alcaldia',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='asamblea',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='concejo',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='gobernacion',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='jal',
            name='observaciones',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='renglon',
            field=models.SmallIntegerField(),
        ),
    ]
