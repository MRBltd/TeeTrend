# Generated by Django 4.2.7 on 2023-12-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='age',
            field=models.CharField(choices=[('6-18m', '6-18m'), ('18-24m', '18-24m'), ('2-4y', '2-4y'), ('4-6y', '4-6y'), ('6-8y', '6-8y'), ('8-9y', '8-9y'), ('9-10y', '9-10y'), ('10-11y', '10-11y'), ('11-12y', '11-12y'), ('12-13y', '12-13y'), ('13-14y', '13-14y'), ('14-15y', '14-15y'), ('2-3y', '2-3y'), ('3-4y', '3-4y'), ('4-5y', '4-5y'), ('5-6y', '5-6y'), ('6-7y', '6-7y'), ('7-8y', '7-8y'), ('8-10y', '8-10y'), ('10-12y', '10-12y'), ('12-14y', '12-14y'), ('14-16y', '14-16y')], max_length=6),
        ),
    ]
