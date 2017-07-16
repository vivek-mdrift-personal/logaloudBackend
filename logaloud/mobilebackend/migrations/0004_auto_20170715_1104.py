# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 11:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobilebackend', '0003_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('additional_info', models.CharField(max_length=500)),
                ('ally', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mobilebackend.Listing')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilebackend.Listing')),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perk_name', models.CharField(max_length=100)),
                ('perk_description', models.CharField(max_length=200)),
                ('perk_coupon_code', models.CharField(max_length=7)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('perk_image_url', models.CharField(max_length=200)),
                ('additional_info', models.CharField(max_length=500)),
                ('ally', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mobilebackend.Listing')),
                ('from_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilebackend.Listing')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=30)),
                ('trip_description', models.CharField(max_length=255)),
                ('trip_start_date', models.DateTimeField()),
                ('trip_end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('trip_image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TripItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tripItem_start_date', models.DateTimeField()),
                ('tripItem_end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('tripItem_image', models.CharField(max_length=200)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilebackend.Listing')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilebackend.Trip')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mobilebackend.Role'),
        ),
    ]