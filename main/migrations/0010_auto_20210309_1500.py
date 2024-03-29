# Generated by Django 3.1.6 on 2021-03-09 15:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_user_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_donor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nid_image',
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10}$')])),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, help_text='YYYY/MM/DD - eg: 1998/02/27', null=True)),
                ('nid_image', models.FileField(blank=True, null=True, upload_to='static/assets/nid/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
