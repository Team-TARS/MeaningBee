# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MeaningBeeApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='comment',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='store',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
