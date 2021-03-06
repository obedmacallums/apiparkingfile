# Generated by Django 3.2.7 on 2021-11-26 22:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0018_alter_entry_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigAlert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_pattern', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^[0-9A-Z]*$', 'Only uppercase letters and numbers are allowed, no spaces or special characters.')])),
                ('active', models.BooleanField(default=True)),
                ('alert_time', models.JSONField()),
                ('precision', models.IntegerField(choices=[(0, 'Equal'), (1, 'Over 80'), (2, 'Over 60')])),
                ('match_by_category', models.BooleanField(default=False)),
                ('any_plate', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.camera')),
                ('category', models.ManyToManyField(default=None, to='core.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
