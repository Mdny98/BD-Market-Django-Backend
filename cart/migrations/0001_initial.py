# Generated by Django 3.0.8 on 2020-08-29 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('Supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('u', 'Unfinilized'), ('f', 'Finalized')], default='u', max_length=1)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(default=0)),
                ('number', models.IntegerField(default=0)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cart.Cart')),
                ('product_supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Supplier.ProductSupplier')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='delivery_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.Delivery'),
        ),
    ]
