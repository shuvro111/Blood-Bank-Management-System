# Generated by Django 3.2 on 2021-04-15 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_donor_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='is_available',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
