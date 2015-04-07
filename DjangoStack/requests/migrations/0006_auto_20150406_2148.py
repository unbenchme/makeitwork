# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_auto_20150406_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='available',
            name='username',
        ),
        migrations.DeleteModel(
            name='Available',
        ),
        migrations.RemoveField(
            model_name='requestaccept',
            name='request_id',
        ),
        migrations.RemoveField(
            model_name='requestaccept',
            name='username',
        ),
        migrations.DeleteModel(
            name='RequestAccept',
        ),
        migrations.RemoveField(
            model_name='category',
            name='username',
        ),
        migrations.RemoveField(
            model_name='request',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_timestamp',
        ),
        migrations.AddField(
            model_name='request',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 7, 2, 48, 27, 718000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=b'A Category', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
