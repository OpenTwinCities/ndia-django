# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=100)),
                ('event_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat_lon_json', djgeojson.fields.PointField()),
                ('Org_address', models.CharField(max_length=240)),
                ('Org_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='event_place',
            field=models.ForeignKey(to='communityAssets.Organization'),
            preserve_default=True,
        ),
    ]
