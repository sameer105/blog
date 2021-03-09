# Generated by Django 3.1.7 on 2021-03-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custuser',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='custuser',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='custuser',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='custuser',
            name='password1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='custuser',
            name='password2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='custuser',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
