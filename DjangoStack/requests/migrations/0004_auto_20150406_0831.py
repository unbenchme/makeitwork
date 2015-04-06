# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requests', '0003_auto_20150405_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='available',
            old_name='username',
            new_name='username_id',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='username',
            new_name='username_id',
        ),
        migrations.RenameField(
            model_name='requestaccept',
            old_name='username',
            new_name='username_id',
        ),
        migrations.AddField(
            model_name='category',
            name='category_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 13, 31, 45, 397000, tzinfo=utc), verbose_name=datetime.datetime(2015, 4, 6, 13, 31, 23, 479000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='username_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='request_timestamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 4, 6, 13, 31, 23, 479000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
