# Generated by Django 2.0.10 on 2019-02-07 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo_scanner', '0010_auto_20190207_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scantask',
            name='file_obj',
            field=models.FilePathField(allow_folders=True, max_length=300, recursive=True),
        ),
    ]