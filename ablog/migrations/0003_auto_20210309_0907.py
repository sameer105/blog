# Generated by Django 3.1.7 on 2021-03-09 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0002_auto_20210309_0855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='custuser',
        ),
    ]