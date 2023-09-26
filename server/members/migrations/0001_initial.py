# Generated by Django 4.2.3 on 2023-09-26 02:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('approved', models.BooleanField(default=False)),
                ('company_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.CharField(max_length=255)),
                ('po_number', models.IntegerField(default=0)),
                ('load_type', models.CharField(choices=[('Full', 'Full'), ('LTL', 'LTL'), ('Container', 'Container')], default='Full', max_length=32)),
                ('container_number', models.IntegerField(blank=True, null=True)),
                ('note_section', models.CharField(blank=True, max_length=512, null=True)),
                ('date_time', models.DateTimeField(verbose_name='Request Date')),
                ('delivery', models.BooleanField(default=False)),
                ('trailer_number', models.CharField(blank=True, max_length=32, null=True)),
                ('driver_phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('dock_number', models.IntegerField(blank=True, null=True)),
                ('check_in_time', models.TimeField(blank=True, null=True, verbose_name='Checked In')),
                ('docked_time', models.TimeField(blank=True, null=True, verbose_name='Docked Time')),
                ('completed_time', models.TimeField(blank=True, null=True, verbose_name='Time Completed')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
                ('phone_number', models.CharField(max_length=12)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('approver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.request')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='request',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.warehouse'),
        ),
    ]
