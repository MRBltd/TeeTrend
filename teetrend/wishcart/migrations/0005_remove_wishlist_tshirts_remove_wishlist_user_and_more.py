# Generated by Django 4.2.7 on 2024-01-31 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishcart', '0004_remove_cart_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='tshirts',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]