# Generated by Django 3.2.7 on 2021-09-09 02:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Date Update')),
                ('is_active', models.BooleanField(default=True, verbose_name='State')),
                ('unique_code', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Code Unique Generate')),
                ('description', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Base Model',
                'verbose_name_plural': 'Base Models',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Date Update')),
                ('is_active', models.BooleanField(default=True, verbose_name='State')),
                ('unique_code', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Code Unique Generate')),
                ('identifyCatrastal', models.CharField(max_length=250, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('identify', models.CharField(max_length=250, unique=True)),
                ('typeProperty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.typeproperty')),
            ],
            options={
                'verbose_name': 'Base Model',
                'verbose_name_plural': 'Base Models',
                'abstract': False,
            },
        ),
    ]
