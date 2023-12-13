# Generated by Django 4.2.7 on 2023-12-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_tshirt_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='category',
            field=models.CharField(blank=True, choices=[('MT', 'Men T-Shirts'), ('WT', 'Women T-Shirts'), ('KT', 'Kids T-Shirts'), ('CT', 'Characters')], max_length=2),
        ),
        migrations.AlterField(
            model_name='tshirt',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('PN', 'Polo Neck'), ('HS', 'Half Sleeves'), ('HLN', 'Henley Neck'), ('HD', 'Hoodies'), ('SL', 'Sleeveless'), ('SW', 'Sweatshirts'), ('LS', 'Long Sleeves'), ('PT', 'Printed T-Shirts'), ('CBT', 'Colorblock T-Shirts'), ('VN', 'V-Neck'), ('WN', 'Wide Neck Off Shoulder T-shirts'), ('YN', 'Yoke Neck T-shirts'), ('DB', 'Douche Bag Neck T-shirt'), ('PLN', 'Plunge Neck'), ('CS', 'Cold Shoulder'), ('HN', 'High Neck'), ('CT', 'Collared T-shirts'), ('BW', 'Basic White T-Shirts'), ('BT', 'Boyfriend tees'), ('ST', 'Striped T-Shirts'), ('KC', 'Knot Crop'), ('SN', 'Scoop Neck'), ('CN', 'Crew Neck')], max_length=3),
        ),
    ]
