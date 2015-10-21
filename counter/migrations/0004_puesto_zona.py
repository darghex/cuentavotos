# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='zona',
            field=models.ForeignKey(default=1, to='counter.Zona'),
            preserve_default=False,
        ),
    ]
