# Generated by Django 2.2.3 on 2019-08-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190825_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]