# Generated by Django 3.2.8 on 2021-11-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_bookissue_dues_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
