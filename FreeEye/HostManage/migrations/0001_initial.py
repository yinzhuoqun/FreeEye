# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SystemManage', '0001_initial'),
        ('AlertManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appName', models.CharField(max_length=32)),
                ('cmdline', models.CharField(max_length=32)),
                ('cmdArgs', models.CharField(max_length=128)),
                ('startCommand', models.CharField(max_length=256)),
                ('stopCommand', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=128)),
                ('port', models.IntegerField(default=22)),
                ('password', models.CharField(max_length=64)),
                ('remark', models.TextField(blank=True, default='', max_length=128)),
                ('active', models.BooleanField(default=False)),
                ('isDel', models.BooleanField(default=False)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('alert', models.ManyToManyField(blank=True, default=None, null=True, to='AlertManage.Alert')),
                ('hostgroup', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemManage.HostGroup')),
            ],
        ),
        migrations.CreateModel(
            name='HostAppliction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_id', models.IntegerField()),
                ('application_id', models.IntegerField()),
                ('status', models.CharField(choices=[('NI', '未安装'), ('OF', '未启动'), ('ON', '运行中')], default='OF', max_length=2)),
                ('updateAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OS', models.CharField(max_length=64)),
                ('cpu_version', models.CharField(max_length=128)),
                ('mem_total', models.IntegerField()),
                ('disk_total', models.CharField(max_length=16)),
                ('kernal_version', models.CharField(max_length=128)),
                ('host', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HostManage.Host')),
            ],
        ),
        migrations.CreateModel(
            name='HostStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_sys', models.FloatField()),
                ('cpu_usr', models.FloatField()),
                ('memTotal', models.IntegerField()),
                ('memUsed', models.IntegerField()),
                ('memFree', models.IntegerField()),
                ('netSend', models.IntegerField()),
                ('netRecv', models.IntegerField()),
                ('diskW', models.IntegerField()),
                ('diskR', models.IntegerField()),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostManage.Host')),
            ],
        ),
    ]