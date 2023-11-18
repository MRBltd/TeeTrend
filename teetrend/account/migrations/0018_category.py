# Generated by Django 4.2.7 on 2023-11-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_useraccount_otp_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MT', 'Men T-Shirts'), ('WT', 'Women T-Shirts'), ('KT', 'Kids T-Shirts'), ('CH', 'Characters')], default='MT', max_length=2)),
            ],
        ),
    ]
