# Generated by Django 4.2.7 on 2023-11-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]