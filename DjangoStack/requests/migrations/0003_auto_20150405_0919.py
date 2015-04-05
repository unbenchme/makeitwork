# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20150405_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='available',
            name='is_available',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
