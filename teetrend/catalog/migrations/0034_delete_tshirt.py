# Generated by Django 4.2.7 on 2024-01-31 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishcart', '0005_remove_wishlist_tshirts_remove_wishlist_user_and_more'),
        ('catalog', '0033_delete_wishlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tshirt',
        ),
    ]