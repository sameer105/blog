# Generated by Django 3.1.6 on 2021-02-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0002_auto_20210214_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog.....', max_length=255),
        ),
    ]
