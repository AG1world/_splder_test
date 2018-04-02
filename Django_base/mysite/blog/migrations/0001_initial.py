# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('au_name', models.CharField(max_length=30)),
                ('au_age', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('pub_date', models.DateField()),
                ('author', models.CharField(max_length=30)),
                ('authors', models.ManyToManyField(to='blog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(to='blog.Publish'),
        ),
    ]
