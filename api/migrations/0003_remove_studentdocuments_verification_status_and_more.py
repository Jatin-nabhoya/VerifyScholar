# Generated by Django 4.1 on 2022-08-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_studentdocuments_verification_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdocuments',
            name='verification_status',
        ),
        migrations.AddField(
            model_name='user',
            name='verification_status',
            field=models.BooleanField(default=False),
        ),
    ]
