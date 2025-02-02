# Generated by Django 3.2 on 2024-05-31 09:25

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('trend1', models.CharField(max_length=255)),
                ('trend2', models.CharField(max_length=255)),
                ('trend3', models.CharField(max_length=255)),
                ('trend4', models.CharField(max_length=255)),
                ('trend5', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
    ]
