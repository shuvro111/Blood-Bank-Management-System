# Generated by Django 3.1.7 on 2021-03-19 16:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank', '0004_auto_20210319_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=50)),
                ('donor_name', models.EmailField(max_length=50)),
                ('donor_mobile_no', models.CharField(max_length=254)),
                ('donation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('blood_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood_bank.bloodbank')),
            ],
        ),
    ]