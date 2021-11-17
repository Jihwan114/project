# Generated by Django 3.2.7 on 2021-11-17 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Puppy',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('kind', models.CharField(max_length=200, null=True)),
                ('Primary_weight', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('neutralization', models.BooleanField(default=True)),
                ('birth_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('animal_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
