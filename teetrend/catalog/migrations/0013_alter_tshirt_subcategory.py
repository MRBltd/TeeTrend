# Generated by Django 4.2.7 on 2023-12-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_alter_tshirt_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='subcategory',
            field=models.CharField(choices=[('PN', 'Polo Neck'), ('HS', 'Half Sleeves'), ('HLN', 'Henley Neck'), ('HD', 'Hoodies'), ('SL', 'Sleeveless'), ('SW', 'Sweatshirts'), ('LS', 'Long Sleeves'), ('PT', 'Printed T-Shirts'), ('CBT', 'Colorblock T-Shirts'), ('VN', 'V-Neck'), ('WN', 'Wide Neck Off Shoulder T-shirts'), ('YN', 'Yoke Neck T-shirts'), ('DB', 'Douche Bag Neck T-shirt'), ('PLN', 'Plunge Neck'), ('CS', 'Cold Shoulder'), ('HN', 'High Neck'), ('CT', 'Collared T-shirts'), ('BW', 'Basic White T-Shirts'), ('BT', 'Boyfriend tees'), ('ST', 'Striped T-Shirts'), ('KC', 'Knot Crop'), ('SN', 'Scoop Neck'), ('CN', 'Crew Neck')], default='PN', max_length=3),
        ),
    ]
