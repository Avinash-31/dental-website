# Generated by Django 5.0.1 on 2024-02-01 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_reviews_profession'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='appointments',
            new_name='appointment',
        ),
        migrations.RenameModel(
            old_name='dentists',
            new_name='dentist',
        ),
        migrations.RenameModel(
            old_name='reviews',
            new_name='review',
        ),
    ]
