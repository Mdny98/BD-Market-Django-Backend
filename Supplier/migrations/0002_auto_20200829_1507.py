# Generated by Django 3.0.8 on 2020-08-29 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
        ('accounts', '0001_initial'),
        ('Supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsupplier',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Product'),
        ),
        migrations.AddField(
            model_name='productsupplier',
            name='supplier_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='accounts.Supplier'),
        ),
    ]
