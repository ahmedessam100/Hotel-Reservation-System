# Generated by Django 2.1.4 on 2018-12-20 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
        ('Reservation', '0004_auto_20181220_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklisted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(verbose_name='Date')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer')),
            ],
        ),
    ]