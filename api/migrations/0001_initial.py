
# Generated by Django 4.1 on 2022-08-26 04:57


import api.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('refreshtoken', models.CharField(default=None, max_length=255, null=True)),
                ('vpass', models.SmallIntegerField(default=0, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FormDetails',
            fields=[
                ('sid', models.OneToOneField(db_column='sid', default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('disablity', models.BooleanField(default=False)),
                ('coaching_required', models.CharField(max_length=70)),
                ('qualification', models.CharField(max_length=70)),
                ('qualification_status', models.CharField(choices=[('Appearing', 'Appearing'), ('Passed', 'Passed')], max_length=10)),
                ('bank_accountholder_name', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=30)),
                ('bank_account_no', models.CharField(max_length=20)),
                ('bank_IFSC_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('sid', models.OneToOneField(db_column='sid', default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nsp_id', models.CharField(max_length=20, null=True)),
                ('aadhaar_no', models.CharField(default=None, max_length=12)),
                ('pms_benificiary_id', models.CharField(max_length=20, null=True)),
                ('caste_category', models.CharField(choices=[('sc', 'SC'), ('obc', 'OBC')], default='--Select--', max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(default=None, max_length=12)),
                ('date_of_registration', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_of_lastupdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDocuments',
            fields=[
                ('sid', models.OneToOneField(db_column='sid', default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('inc_status', models.CharField(default=None, max_length=30, null=True)),
                ('aadhaar_status', models.CharField(default=None, max_length=30, null=True)),
                ('creamy_status', models.CharField(default=None, max_length=30, null=True)),
                ('marksheet10_status', models.CharField(default=None, max_length=30, null=True)),
                ('marksheet12_status', models.CharField(default=None, max_length=30, null=True)),
                ('disability_status', models.CharField(default=None, max_length=30, null=True)),
                ('vpass', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StuDocAdmin',
            fields=[
                ('sid', models.OneToOneField(db_column='sid', default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('incomecertificate', models.FileField(default=None, upload_to=api.models.StuDocAdmin.use_directory_path)),
                ('auid', models.SmallIntegerField(default=None)),
                ('aname', models.CharField(default=None, max_length=50, null=True)),
                ('agender', models.CharField(default=None, max_length=1, null=True)),
                ('aaddress', models.CharField(default=None, max_length=255, null=True)),
                ('adob', models.DateField(default=None, null=True)),
                ('noncreamylayer', models.FileField(default=None, upload_to=api.models.StuDocAdmin.use_directory_path)),
                ('marksheet10', models.FileField(default=None, upload_to=api.models.StuDocAdmin.use_directory_path)),
                ('marksheet12', models.FileField(default=None, upload_to=api.models.StuDocAdmin.use_directory_path)),
                ('disabilitycert', models.FileField(default=None, upload_to=api.models.StuDocAdmin.use_directory_path)),
            ],
        ),
    ]
