# Generated by Django 3.2.7 on 2021-10-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211017_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='key_file_name',
            new_name='ssh_key_file_name',
        ),
    ]
