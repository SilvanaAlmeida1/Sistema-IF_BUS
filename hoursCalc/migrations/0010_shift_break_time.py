# Generated by Django 3.0 on 2022-06-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoursCalc', '0009_remove_shift_break_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='break_time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
