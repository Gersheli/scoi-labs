# Generated by Django 4.2.1 on 2023-05-17 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_purchase_count'),
        ('order', '0002_remove_order_paid_remove_order_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.product'),
        ),
    ]