# Generated by Django 4.2.4 on 2023-08-21 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thinkify', '0004_rename_date_scholarship_examdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exams',
            old_name='exam',
            new_name='examname',
        ),
    ]
