# Generated by Django 3.1.6 on 2021-02-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210228_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_donor',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
