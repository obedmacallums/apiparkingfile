# Generated by Django 3.2.7 on 2021-10-18 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_key_file_name_agent_ssh_key_file_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camera',
            old_name='local_link',
            new_name='local_link1',
        ),
    ]
