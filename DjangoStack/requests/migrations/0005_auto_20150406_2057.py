# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.auth.models
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requests', '0004_auto_20150406_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available',
            name='username_id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_timestamp',
        ),
        migrations.RemoveField(
            model_name='category',
            name='username_id',
        ),
        migrations.RemoveField(
            model_name='request',
            name='username_id',
        ),
        migrations.RemoveField(
            model_name='requestaccept',
            name='username_id',
        ),
        migrations.AddField(
            model_name='available',
            name='username',
            field=models.ForeignKey(related_name='available_username', default=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 1, 57, 54, 689000, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='username',
            field=models.ForeignKey(related_name='category_created_by', default=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='created_by',
            field=models.ForeignKey(related_name='request_created_by', default=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='request',
            name='name',
            field=models.CharField(default=b'A Project', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requestaccept',
            name='username',
            field=models.ForeignKey(related_name='request_accept_username', default=django.contrib.auth.models.User, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='available',
            name='is_available',
            field=models.BooleanField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='request',
            name='request_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 1, 57, 54, 689000, tzinfo=utc), editable=False),
            preserve_default=True,
        ),
    ]
