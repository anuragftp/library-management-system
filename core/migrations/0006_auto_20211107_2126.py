# Generated by Django 3.2.8 on 2021-11-07 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_student_year'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dues',
            new_name='Due',
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]
