# Generated by Django 4.1.5 on 2023-10-13 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login1',
            new_name='login',
        ),
        migrations.RenameModel(
            old_name='signup1',
            new_name='signup',
        ),
    ]
