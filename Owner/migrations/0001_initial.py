# Generated by Django 2.1.4 on 2018-12-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='', max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('mobileNumber', models.CharField(max_length=15)),
            ],
        ),
    ]