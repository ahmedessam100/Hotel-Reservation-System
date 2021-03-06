# Generated by Django 2.1.4 on 2018-12-12 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Location', '0001_initial'),
        ('Owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('singleRoomsCount', models.IntegerField(default=0)),
                ('doubleRoomsCount', models.IntegerField(default=0)),
                ('singelRoomsPrice', models.IntegerField(default=0)),
                ('doubleRoomsPrice', models.IntegerField(default=0)),
                ('stars', models.IntegerField()),
                ('image', models.ImageField(upload_to=None)),
                ('hotel_location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Location.location')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.owner')),
            ],
        ),
    ]
