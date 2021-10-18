# Generated by Django 3.2.7 on 2021-10-10 17:09

import core.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211006_0020'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9A-Z\\s-]*$', 'Only uppercase letters, numbers and spaces allowed')])),
                ('camera_id', models.PositiveIntegerField()),
                ('local_link', core.models.LocalURLField(blank=True, max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.domain')),
            ],
        ),
    ]
