# Generated by Django 2.0.10 on 2019-02-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo_scanner', '0011_auto_20190207_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scantask',
            name='file_obj',
            field=models.FilePathField(allow_files=False, allow_folders=True, max_length=300, recursive=True),
        ),
    ]