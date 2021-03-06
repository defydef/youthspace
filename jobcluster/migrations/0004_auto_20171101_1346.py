# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobcluster', '0003_question_q_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='question',
            name='q_img',
            field=models.ImageField(blank=True, upload_to='img/question'),
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='jobcluster.Question'),
        ),
    ]
