# Generated by Django 5.0.1 on 2024-02-01 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_message_dateofappointment_alter_message_slot'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='message',
            new_name='appointments',
        ),
    ]