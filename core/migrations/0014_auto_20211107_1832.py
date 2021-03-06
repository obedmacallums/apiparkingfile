# Generated by Django 3.2.7 on 2021-11-07 18:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20211019_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_data', models.JSONField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='addedinfo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category'),
        ),
        migrations.AddField(
            model_name='addedinfo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addedinfo',
            name='custom_fields',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addedinfo',
            name='driver_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='addedinfo',
            name='driver_name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[0-9A-Z\\s-]*$', 'Only uppercase letters, numbers and spaces allowed')]),
        ),
        migrations.AddField(
            model_name='addedinfo',
            name='plate',
            field=models.CharField(default=None, max_length=8, validators=[django.core.validators.RegexValidator('^[0-9A-Z]*$', 'Only uppercase letters and numbers are allowed, no spaces or special characters.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addedinfo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.agent'),
        ),
        migrations.AddField(
            model_name='entry',
            name='best_uuid',
            field=models.CharField(blank=True, default='1', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='camara',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.camera'),
        ),
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category'),
        ),
        migrations.AddField(
            model_name='entry',
            name='confidence',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='crop_image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='custom_fields',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='driver_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='driver_name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[0-9A-Z\\s-]*$', 'Only uppercase letters, numbers and spaces allowed')]),
        ),
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='is_parked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='is_preview',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='link_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='plate',
            field=models.CharField(default=None, max_length=8, validators=[django.core.validators.RegexValidator('^[0-9A-Z]*$', 'Only uppercase letters and numbers are allowed, no spaces or special characters.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='travel_direction',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='vehicle',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='vehicle_detected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='entry',
            name='meta_data',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.metadata'),
        ),
    ]
