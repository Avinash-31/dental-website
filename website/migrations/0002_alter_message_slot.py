# Generated by Django 5.0.1 on 2024-02-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='slot',
            field=models.CharField(choices=[('', 'Enter your preferred slot'), ('9 AM to 10 AM', '9 AM to 10 AM'), ('11 AM to 12 PM', '11 AM to 12 PM'), ('2 PM to 4 PM', '2 PM to 4 PM')], default='Select your preferred slot', max_length=20),
        ),
    ]