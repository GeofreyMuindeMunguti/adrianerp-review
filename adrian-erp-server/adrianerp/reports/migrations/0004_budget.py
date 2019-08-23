# Generated by Django 2.2.3 on 2019-08-23 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20190818_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('beneficiary_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('phoneNumber', models.CharField(max_length=100)),
                ('unit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='reports.Site')),
            ],
        ),
    ]