# Generated by Django 3.1.6 on 2021-02-05 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='User',
        ),
    ]
