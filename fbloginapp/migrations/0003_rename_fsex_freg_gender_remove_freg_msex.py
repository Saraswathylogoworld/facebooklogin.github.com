# Generated by Django 4.0 on 2022-02-08 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbloginapp', '0002_rename_day_freg_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freg',
            old_name='fsex',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='freg',
            name='msex',
        ),
    ]
