# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_in_hours', models.DecimalField(max_digits=4, decimal_places=2)),
                ('request_timestamp', models.DateTimeField()),
                ('number_of_people', models.DecimalField(max_digits=2, decimal_places=0)),
                ('category_name', models.ForeignKey(to='requests.Category')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='requests',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='username',
        ),
        migrations.AlterField(
            model_name='requestaccept',
            name='request_id',
            field=models.ForeignKey(to='requests.Request'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Requests',
        ),
    ]
