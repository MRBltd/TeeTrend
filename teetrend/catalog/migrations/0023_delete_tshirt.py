# Generated by Django 4.2.7 on 2023-12-10 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_alter_tshirt_category_alter_tshirt_subcategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tshirt',
        ),
    ]
