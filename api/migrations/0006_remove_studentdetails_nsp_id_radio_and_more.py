# Generated by Django 4.1 on 2022-08-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_studentdocuments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='nsp_id_radio',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='pms_benificiary_id_radio',
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='sid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
