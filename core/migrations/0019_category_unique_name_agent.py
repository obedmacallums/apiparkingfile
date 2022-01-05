# Generated by Django 3.2.7 on 2021-11-30 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_entry_category'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name', 'agent'), name='unique_name_agent'),
        ),
    ]
