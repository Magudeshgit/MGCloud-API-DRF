# Generated by Django 4.1.3 on 2024-06-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_users_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='file',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='filename',
            field=models.CharField(default='sample', max_length=100),
            preserve_default=False,
        ),
    ]