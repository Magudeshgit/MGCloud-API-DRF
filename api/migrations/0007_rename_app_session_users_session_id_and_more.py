# Generated by Django 4.1.3 on 2024-07-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_fileupload_file_fileupload_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='app_session',
            new_name='session_id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='MGRID',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
    ]
