# Generated by Django 2.0.10 on 2019-02-07 20:10

from django.conf import settings
from django.db import migrations, models
import recurrence.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repo_scanner', '0004_auto_20190204_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_root', models.CharField(max_length=300)),
                ('scan_slug', models.CharField(max_length=100)),
                ('scan_desc', models.CharField(max_length=500)),
                ('recurrence', recurrence.fields.RecurrenceField()),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.OneToOneField(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
