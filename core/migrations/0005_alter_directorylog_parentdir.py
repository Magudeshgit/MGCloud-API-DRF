# Generated by Django 4.1.3 on 2024-09-07 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_directorylog_issubdir_alter_directorylog_filecount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directorylog',
            name='parentDir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.directorylog'),
        ),
    ]
