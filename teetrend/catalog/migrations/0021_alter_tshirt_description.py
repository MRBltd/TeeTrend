# Generated by Django 4.2.7 on 2023-12-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_tshirt_characters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]