# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_start', models.DateTimeField()),
                ('game_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GameRound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_round_start', models.DateTimeField()),
                ('game_round_end', models.DateTimeField()),
                ('game', models.ForeignKey(to='MeaningBeeApp.Game')),
            ],
        ),
        migrations.CreateModel(
            name='GameRound_User_Mapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_meaning_completed', models.BooleanField(default=False)),
                ('is_judging_completed', models.BooleanField(default=False)),
                ('judging_score', models.IntegerField()),
                ('meaning_score', models.IntegerField()),
                ('game_round', models.ForeignKey(to='MeaningBeeApp.GameRound')),
            ],
        ),
        migrations.CreateModel(
            name='GameRound_User_Meaning_Judgement_Mapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameRound_User_Meaning_Mapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_meaning', models.CharField(max_length=2000)),
                ('game_round_user', models.ForeignKey(to='MeaningBeeApp.GameRound_User_Mapping')),
            ],
        ),
        migrations.CreateModel(
            name='Judgement_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('judgement_type', models.CharField(default=b'UNSURE', max_length=100, choices=[(b'CORRECT', b'CORRECT'), (b'INCORRECT', b'INCORRECT'), (b'CORRECT_NOT_IN_DICTIONARY', b'CORRECT_NOT_IN_DICTIONARY'), (b'UNSURE', b'UNSURE')])),
            ],
        ),
        migrations.CreateModel(
            name='Objection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isScoreChanged', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateTimeField()),
                ('user', models.OneToOneField(related_name='user_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertype_name', models.CharField(default=b'PLAYER', max_length=10, choices=[(b'ADMIN', b'ADMIN'), (b'PLAYER', b'PLAYER')])),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WordMeaning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_of_speech', models.CharField(max_length=30)),
                ('meaning', models.CharField(max_length=2000)),
                ('isPlayerSuggested', models.BooleanField(default=False)),
                ('word', models.ForeignKey(to='MeaningBeeApp.Word')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='usertype',
            field=models.ForeignKey(to='MeaningBeeApp.UserType'),
        ),
        migrations.AddField(
            model_name='objection',
            name='addressed_by',
            field=models.ForeignKey(related_name='objection_addressed_by', to='MeaningBeeApp.UserProfile'),
        ),
        migrations.AddField(
            model_name='objection',
            name='gameround_user_meaning_judgement',
            field=models.ForeignKey(to='MeaningBeeApp.GameRound_User_Meaning_Judgement_Mapping'),
        ),
        migrations.AddField(
            model_name='objection',
            name='raised_by',
            field=models.ForeignKey(related_name='objection_raised_by', to='MeaningBeeApp.UserProfile'),
        ),
        migrations.AddField(
            model_name='gameround_user_meaning_judgement_mapping',
            name='gameround_user_meaning',
            field=models.ForeignKey(to='MeaningBeeApp.GameRound_User_Meaning_Mapping'),
        ),
        migrations.AddField(
            model_name='gameround_user_meaning_judgement_mapping',
            name='judge',
            field=models.ForeignKey(to='MeaningBeeApp.UserProfile'),
        ),
        migrations.AddField(
            model_name='gameround_user_meaning_judgement_mapping',
            name='judgement_type',
            field=models.ForeignKey(to='MeaningBeeApp.Judgement_Type'),
        ),
        migrations.AddField(
            model_name='gameround_user_meaning_judgement_mapping',
            name='system_meaning',
            field=models.ForeignKey(to='MeaningBeeApp.WordMeaning'),
        ),
        migrations.AddField(
            model_name='gameround_user_mapping',
            name='user',
            field=models.ForeignKey(to='MeaningBeeApp.UserProfile'),
        ),
        migrations.AddField(
            model_name='gameround',
            name='word',
            field=models.ForeignKey(to='MeaningBeeApp.Word'),
        ),
    ]
