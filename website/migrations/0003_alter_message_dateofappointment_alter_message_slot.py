# Generated by Django 5.0.1 on 2024-02-01 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_message_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='dateOfAppointment',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='slot',
            field=models.CharField(default='Select your preferred slot', max_length=20),
        ),
    ]
