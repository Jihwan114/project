# Generated by Django 3.2.7 on 2021-11-17 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avg_Weight',
            fields=[
                ('category_code', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('max_weight', models.FloatField(blank=True, default=0.0)),
                ('min_weight', models.FloatField(blank=True, default=0.0)),
                ('avg_weight', models.FloatField(blank=True, default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Health_Check_Schedule',
            fields=[
                ('month', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('health_check_list', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puppy_life_Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_life', models.TextField()),
                ('walk_around', models.TextField()),
                ('sanitary', models.TextField()),
                ('food_and_etc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(default=0)),
                ('category_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.avg_weight')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('confirm_password', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('login_fail_count', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'user_id',
            },
        ),
    ]
