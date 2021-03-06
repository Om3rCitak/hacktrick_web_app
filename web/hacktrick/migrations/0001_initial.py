# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CFP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ConferenceSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='contributor/')),
                ('title', models.CharField(max_length=100)),
                ('mission', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField()),
                ('url', models.URLField()),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Şehir')),
                ('place_fullname', models.CharField(max_length=150, verbose_name='Konum tam')),
                ('expected_participant', models.PositiveIntegerField(verbose_name='Beklenen katılımcı sayısı')),
                ('expected_speaker', models.PositiveIntegerField(verbose_name='Beklenen konuşmacı sayısı')),
                ('place', models.CharField(help_text="Anasayfa'da görünmesini istediğiniz şekilde yazınız.", max_length=100, verbose_name='Konum kısa')),
                ('date', models.CharField(help_text="Anasayfa'da görünmesini istediğiniz şekilde yazınız.", max_length=100, verbose_name='Tarih')),
                ('starting_date', models.DateTimeField(verbose_name='Başlangıç tarihi')),
                ('address', models.TextField(help_text='Google code')),
                ('about', models.TextField(help_text='HTML kodu yazabilirsiniz.', verbose_name='Hakkında')),
            ],
        ),
        migrations.CreateModel(
            name='Speak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('starting_time', models.TimeField()),
                ('ending_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='Ad soyad')),
                ('image', models.ImageField(help_text='160x160', upload_to='speaker/', verbose_name='Resim')),
                ('title', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100, verbose_name='Kurum')),
                ('facebook', models.CharField(blank=True, help_text='facebook kullanıcı adı', max_length=50)),
                ('twitter', models.CharField(blank=True, help_text='twitter kullanıcı adı', max_length=50)),
                ('linkedin', models.CharField(blank=True, help_text='linkedin kullanıcı adı', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.SmallIntegerField(choices=[(0, 'Platin'), (1, 'Altın'), (2, 'Gümüş'), (3, 'Destekleyenler'), (4, 'Medya')])),
                ('image', models.ImageField(help_text='370x190', upload_to='sponsor/')),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cover_image', models.ImageField(upload_to='training/')),
                ('content', models.TextField()),
                ('capacity', models.PositiveIntegerField()),
                ('reserve_quota', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='document/')),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted_selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_accepted_trainings', related_query_name='user_accepted_training', to='hacktrick.Training')),
                ('first_selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_first_trainings', related_query_name='user_first_training', to='hacktrick.Training')),
                ('second_selection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_second_trainings', related_query_name='user_second_training', to='hacktrick.Training')),
            ],
        ),
    ]
