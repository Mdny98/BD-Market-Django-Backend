# Generated by Django 3.0.8 on 2020-08-11 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20200809_1205'),
        ('content', '0006_remove_product_unit_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='custumer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.CustomerProfile'),
        ),
    ]
