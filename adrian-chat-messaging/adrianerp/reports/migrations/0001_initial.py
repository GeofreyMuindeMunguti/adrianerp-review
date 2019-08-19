# Generated by Django 2.2.4 on 2019-08-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(max_length=100)),
                ('issue_image', models.ImageField(blank=True, null=True, upload_to='images/InstallationTeam/issues/%Y/%m/%d/')),
                ('issue_sorted_image', models.ImageField(blank=True, null=True, upload_to='images/InstallationTeam/issues/%Y/%m/%d/')),
                ('closed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
