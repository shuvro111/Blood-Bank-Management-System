# Generated by Django 3.1.6 on 2021-02-05 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=254)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, help_text='YYYY/MM/DD - eg: 1998/02/27', null=True)),
                ('nid_image', models.FileField(blank=True, null=True, upload_to='static/assets/nid/%Y/%m/%d/')),
                ('is_donor', models.BooleanField(default=False)),
                ('auth_token', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
