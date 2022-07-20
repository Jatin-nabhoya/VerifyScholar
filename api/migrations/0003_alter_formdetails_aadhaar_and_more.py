# Generated by Django 4.0.6 on 2022-07-17 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_studentdetails_date_of_lastupdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdetails',
            name='aadhaar',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='formdetails',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Divorced', 'Divorced'), ('Separated', 'Separated')], max_length=10),
        ),
        migrations.AlterField(
            model_name='formdetails',
            name='qualification_status',
            field=models.CharField(choices=[('Appearing', 'Appearing'), ('Passed', 'Passed')], max_length=10),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='date_of_registration',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]