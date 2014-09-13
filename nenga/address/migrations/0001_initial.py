# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import jsonfield.fields
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackLayout',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(primary_key=True, serialize=False, editable=False, max_length=22, blank=True, verbose_name=b'UUID')),
                ('layout_template', models.TextField()),
                ('template_attributes', jsonfield.fields.JSONField(default=__builtin__.dict)),
            ],
            options={
                'db_table': 'back_layout',
                'permissions': (('view_back_layout', 'View BackLayout'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(primary_key=True, serialize=False, editable=False, max_length=22, blank=True, verbose_name=b'UUID')),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=7)),
                ('prefecture', models.CharField(max_length=2, choices=[(b'01', b'\xe5\x8c\x97\xe6\xb5\xb7\xe9\x81\x93'), (b'02', b'\xe9\x9d\x92\xe6\xa3\xae\xe7\x9c\x8c'), (b'03', b'\xe5\xb2\xa9\xe6\x89\x8b\xe7\x9c\x8c'), (b'04', b'\xe5\xae\xae\xe5\x9f\x8e\xe7\x9c\x8c'), (b'05', b'\xe7\xa7\x8b\xe7\x94\xb0\xe7\x9c\x8c'), (b'06', b'\xe5\xb1\xb1\xe5\xbd\xa2\xe7\x9c\x8c'), (b'07', b'\xe7\xa6\x8f\xe5\xb3\xb6\xe7\x9c\x8c'), (b'08', b'\xe8\x8c\xa8\xe5\x9f\x8e\xe7\x9c\x8c'), (b'09', b'\xe6\xa0\x83\xe6\x9c\xa8\xe7\x9c\x8c'), (b'10', b'\xe7\xbe\xa4\xe9\xa6\xac\xe7\x9c\x8c'), (b'11', b'\xe5\x9f\xbc\xe7\x8e\x89\xe7\x9c\x8c'), (b'12', b'\xe5\x8d\x83\xe8\x91\x89\xe7\x9c\x8c'), (b'13', b'\xe6\x9d\xb1\xe4\xba\xac\xe9\x83\xbd'), (b'14', b'\xe7\xa5\x9e\xe5\xa5\x88\xe5\xb7\x9d\xe7\x9c\x8c'), (b'15', b'\xe6\x96\xb0\xe6\xbd\x9f\xe7\x9c\x8c'), (b'16', b'\xe5\xaf\x8c\xe5\xb1\xb1\xe7\x9c\x8c'), (b'17', b'\xe7\x9f\xb3\xe5\xb7\x9d\xe7\x9c\x8c'), (b'18', b'\xe7\xa6\x8f\xe4\xba\x95\xe7\x9c\x8c'), (b'19', b'\xe5\xb1\xb1\xe6\xa2\xa8\xe7\x9c\x8c'), (b'20', b'\xe9\x95\xb7\xe9\x87\x8e\xe7\x9c\x8c'), (b'21', b'\xe5\xb2\x90\xe9\x98\x9c\xe7\x9c\x8c'), (b'22', b'\xe9\x9d\x99\xe5\xb2\xa1\xe7\x9c\x8c'), (b'23', b'\xe6\x84\x9b\xe7\x9f\xa5\xe7\x9c\x8c'), (b'24', b'\xe4\xb8\x89\xe9\x87\x8d\xe7\x9c\x8c'), (b'25', b'\xe6\xbb\x8b\xe8\xb3\x80\xe7\x9c\x8c'), (b'26', b'\xe4\xba\xac\xe9\x83\xbd\xe5\xba\x9c'), (b'27', b'\xe5\xa4\xa7\xe9\x98\xaa\xe5\xba\x9c'), (b'28', b'\xe5\x85\xb5\xe5\xba\xab\xe7\x9c\x8c'), (b'29', b'\xe5\xa5\x88\xe8\x89\xaf\xe7\x9c\x8c'), (b'30', b'\xe5\x92\x8c\xe6\xad\x8c\xe5\xb1\xb1\xe7\x9c\x8c'), (b'31', b'\xe9\xb3\xa5\xe5\x8f\x96\xe7\x9c\x8c'), (b'32', b'\xe5\xb3\xb6\xe6\xa0\xb9\xe7\x9c\x8c'), (b'33', b'\xe5\xb2\xa1\xe5\xb1\xb1\xe7\x9c\x8c'), (b'34', b'\xe5\xba\x83\xe5\xb3\xb6\xe7\x9c\x8c'), (b'35', b'\xe5\xb1\xb1\xe5\x8f\xa3\xe7\x9c\x8c'), (b'36', b'\xe5\xbe\xb3\xe5\xb3\xb6\xe7\x9c\x8c'), (b'37', b'\xe9\xa6\x99\xe5\xb7\x9d\xe7\x9c\x8c'), (b'38', b'\xe6\x84\x9b\xe5\xaa\x9b\xe7\x9c\x8c'), (b'39', b'\xe9\xab\x98\xe7\x9f\xa5\xe7\x9c\x8c'), (b'40', b'\xe7\xa6\x8f\xe5\xb2\xa1\xe7\x9c\x8c'), (b'41', b'\xe4\xbd\x90\xe8\xb3\x80\xe7\x9c\x8c'), (b'42', b'\xe9\x95\xb7\xe5\xb4\x8e\xe7\x9c\x8c'), (b'43', b'\xe7\x86\x8a\xe6\x9c\xac\xe7\x9c\x8c'), (b'44', b'\xe5\xa4\xa7\xe5\x88\x86\xe7\x9c\x8c'), (b'45', b'\xe5\xae\xae\xe5\xb4\x8e\xe7\x9c\x8c'), (b'46', b'\xe9\xb9\xbf\xe5\x85\x90\xe5\xb3\xb6\xe7\x9c\x8c'), (b'47', b'\xe6\xb2\x96\xe7\xb8\x84\xe7\x9c\x8c')])),
                ('city', models.CharField(unique=True, max_length=256)),
                ('address', models.CharField(max_length=255)),
                ('address2', models.CharField(default=b'', max_length=255, blank=True)),
                ('patner_name', models.CharField(default=b'', max_length=255, blank=True)),
            ],
            options={
                'db_table': 'contact',
                'permissions': (('view_contact', 'View contact'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanActual',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(primary_key=True, serialize=False, editable=False, max_length=22, blank=True, verbose_name=b'UUID')),
                ('plan', models.BooleanField(default=True)),
                ('actual', models.BooleanField(default=True)),
                ('destination', models.ForeignKey(to='address.Contact')),
            ],
            options={
                'db_table': 'plan_actual',
                'permissions': (('view_plan_actual', 'View PlanActual'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', shortuuidfield.fields.ShortUUIDField(primary_key=True, serialize=False, editable=False, max_length=22, blank=True, verbose_name=b'UUID')),
                ('year', models.DecimalField(max_digits=4, decimal_places=0)),
            ],
            options={
                'db_table': 'year',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='planactual',
            name='year',
            field=models.ForeignKey(to='address.Year'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='planactual',
            unique_together=set([('destination', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together=set([('last_name', 'first_name', 'address', 'zip_code')]),
        ),
        migrations.AddField(
            model_name='backlayout',
            name='year',
            field=models.ForeignKey(to='address.Year'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='backlayout',
            unique_together=set([('year',)]),
        ),
    ]
