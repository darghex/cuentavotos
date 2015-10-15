# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alcaldia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mesa', models.SmallIntegerField()),
                ('total_E11', models.SmallIntegerField(help_text=b'Total sufragantes E11', null=True)),
                ('total_urna', models.SmallIntegerField(help_text=b'Total Votos Urna', null=True)),
                ('incinerados', models.SmallIntegerField(help_text=b'Total Votos Incinerados', null=True)),
                ('votos_blancos', models.SmallIntegerField(null=True)),
                ('votos_nulos', models.SmallIntegerField(null=True)),
                ('votos_no_marcaros', models.SmallIntegerField(null=True, verbose_name=b'No marcados')),
            ],
            options={
                'verbose_name': 'Alcaldia',
            },
        ),
        migrations.CreateModel(
            name='Asamblea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mesa', models.SmallIntegerField()),
                ('total_E11', models.SmallIntegerField(help_text=b'Total sufragantes E11', null=True)),
                ('total_urna', models.SmallIntegerField(help_text=b'Total Votos Urna', null=True)),
                ('incinerados', models.SmallIntegerField(help_text=b'Total Votos Incinerados', null=True)),
                ('votos_blancos', models.SmallIntegerField(null=True)),
                ('votos_nulos', models.SmallIntegerField(null=True)),
                ('votos_no_marcaros', models.SmallIntegerField(null=True, verbose_name=b'No marcados')),
            ],
            options={
                'verbose_name': 'Asamblea',
            },
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('renglon', models.CharField(max_length=2)),
                ('documento', models.CharField(unique=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Concejo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mesa', models.SmallIntegerField()),
                ('total_E11', models.SmallIntegerField(help_text=b'Total sufragantes E11', null=True)),
                ('total_urna', models.SmallIntegerField(help_text=b'Total Votos Urna', null=True)),
                ('incinerados', models.SmallIntegerField(help_text=b'Total Votos Incinerados', null=True)),
                ('votos_blancos', models.SmallIntegerField(null=True)),
                ('votos_nulos', models.SmallIntegerField(null=True)),
                ('votos_no_marcaros', models.SmallIntegerField(null=True, verbose_name=b'No marcados')),
            ],
            options={
                'verbose_name': 'Concejo',
            },
        ),
        migrations.CreateModel(
            name='Corporacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Gobernacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mesa', models.SmallIntegerField()),
                ('total_E11', models.SmallIntegerField(help_text=b'Total sufragantes E11', null=True)),
                ('total_urna', models.SmallIntegerField(help_text=b'Total Votos Urna', null=True)),
                ('incinerados', models.SmallIntegerField(help_text=b'Total Votos Incinerados', null=True)),
                ('votos_blancos', models.SmallIntegerField(null=True)),
                ('votos_nulos', models.SmallIntegerField(null=True)),
                ('votos_no_marcaros', models.SmallIntegerField(null=True, verbose_name=b'No marcados')),
            ],
            options={
                'verbose_name': 'Gobernacion',
            },
        ),
        migrations.CreateModel(
            name='JAL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mesa', models.SmallIntegerField()),
                ('total_E11', models.SmallIntegerField(help_text=b'Total sufragantes E11', null=True)),
                ('total_urna', models.SmallIntegerField(help_text=b'Total Votos Urna', null=True)),
                ('incinerados', models.SmallIntegerField(help_text=b'Total Votos Incinerados', null=True)),
                ('votos_blancos', models.SmallIntegerField(null=True)),
                ('votos_nulos', models.SmallIntegerField(null=True)),
                ('votos_no_marcaros', models.SmallIntegerField(null=True, verbose_name=b'No marcados')),
            ],
            options={
                'verbose_name': 'JAL',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=60)),
                ('abreviatura', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=30)),
                ('mesas', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoVoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VotosAlcaldia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votos', models.SmallIntegerField(null=True)),
                ('alcaldia', models.ForeignKey(to='counter.Alcaldia')),
                ('candidato', models.ForeignKey(to='counter.Candidato')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VotosAsamblea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votos', models.SmallIntegerField(null=True)),
                ('asamblea', models.ForeignKey(to='counter.Asamblea')),
                ('candidato', models.ForeignKey(to='counter.Candidato')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VotosConcejo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votos', models.SmallIntegerField(null=True)),
                ('candidato', models.ForeignKey(to='counter.Candidato')),
                ('concejo', models.ForeignKey(to='counter.Concejo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VotosGobernacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votos', models.SmallIntegerField(null=True)),
                ('candidato', models.ForeignKey(to='counter.Candidato')),
                ('gobernacion', models.ForeignKey(to='counter.Gobernacion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VotosJAL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votos', models.SmallIntegerField(null=True)),
                ('candidato', models.ForeignKey(to='counter.Candidato')),
                ('jal', models.ForeignKey(to='counter.JAL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='jal',
            name='puesto',
            field=models.ForeignKey(to='counter.Puesto'),
        ),
        migrations.AddField(
            model_name='gobernacion',
            name='puesto',
            field=models.ForeignKey(to='counter.Puesto'),
        ),
        migrations.AddField(
            model_name='concejo',
            name='puesto',
            field=models.ForeignKey(to='counter.Puesto'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='corporacion',
            field=models.ForeignKey(to='counter.Corporacion'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='localidad',
            field=models.ForeignKey(to='counter.Localidad'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='partido',
            field=models.ForeignKey(to='counter.Partido'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='tipo_voto',
            field=models.ForeignKey(to='counter.TipoVoto'),
        ),
        migrations.AddField(
            model_name='asamblea',
            name='puesto',
            field=models.ForeignKey(to='counter.Puesto'),
        ),
        migrations.AddField(
            model_name='alcaldia',
            name='puesto',
            field=models.ForeignKey(to='counter.Puesto'),
        ),
    ]
