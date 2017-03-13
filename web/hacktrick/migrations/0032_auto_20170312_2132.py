# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0031_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='type',
            field=models.SmallIntegerField(choices=[(0, 'Kayıt'), (1, 'Eğitim seçimi'), (2, 'Eğitim onayı'), (3, 'Eğitimin güncellenmesi'), (4, 'Eğitime döküman eklenmesi'), (5, 'Bir kullanıcının eğitmen olarak işaretlenmesi'), (6, 'Eğitime kesin kayıt olunması'), (7, 'Ticket açılması'), (8, 'Ticketa cevap verilmesi')], unique=True, verbose_name='Mail seçimi'),
        ),
    ]
