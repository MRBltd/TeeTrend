# Generated by Django 4.2.7 on 2023-12-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0030_alter_tshirt_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('PN', 'Polo Neck'), ('HS', 'Half Sleeves'), ('HLN', 'Henley Neck'), ('HD', 'Hoodies'), ('SL', 'Sleeveless'), ('SW', 'Sweatshirts'), ('LS', 'Long Sleeves'), ('PT', 'Printed T-Shirts'), ('CBT', 'Colorblock T-Shirts'), ('VN', 'V-Neck'), ('WN', 'Wide Neck Off Shoulder T-shirts'), ('YN', 'Yoke Neck T-shirts'), ('DB', 'Douche Bag Neck T-shirt'), ('CS', 'Cold Shoulder'), ('OS', 'Off Shoulder'), ('HN', 'High Neck'), ('WT', 'White T-Shirts'), ('BT', 'Boyfriend tees'), ('ST', 'Striped T-Shirts'), ('KC', 'Knot Crop'), ('SN', 'Scoop Neck'), ('CN', 'Crew Neck')], max_length=3),
        ),
    ]
