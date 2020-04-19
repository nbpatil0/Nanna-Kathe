# Generated by Django 3.0.3 on 2020-04-16 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('phone', models.IntegerField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('principal_amt', models.IntegerField(max_length=10)),
                ('start_date', models.DateField(auto_now=True)),
                ('interest', models.IntegerField(max_length=10)),
                ('interest_amt', models.IntegerField(max_length=10, null=True)),
                ('total_amt', models.IntegerField(max_length=12, null=True)),
                ('end_date', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
