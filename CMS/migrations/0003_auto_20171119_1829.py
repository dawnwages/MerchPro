# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailimages', '0019_delete_filter'),
        ('CMS', '0002_blogpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.CharField(db_index=True, max_length=50)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cms_blogpagetag_items', to='taggit.Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='blogpage',
            name='feature_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='thumbnail_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='CMS.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
