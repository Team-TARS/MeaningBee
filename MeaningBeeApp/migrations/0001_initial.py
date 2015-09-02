# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(verbose_name=b'comment_date')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='store',
            field=models.ForeignKey(to='MeaningBeeApp.Store'),
        ),
    ]
