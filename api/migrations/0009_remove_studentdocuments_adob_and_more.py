# Generated by Django 4.1 on 2022-08-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_studentdocuments_adob_studentdocuments_agender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdocuments',
            name='adob',
        ),
        migrations.RemoveField(
            model_name='studentdocuments',
            name='agender',
        ),
        migrations.RemoveField(
            model_name='studentdocuments',
            name='aname',
        ),
        migrations.AlterField(
            model_name='studentdocuments',
            name='aadhar',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
