# Generated by Django 2.1.4 on 2018-12-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
