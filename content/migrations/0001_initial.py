# Generated by Django 3.0.8 on 2020-08-02 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attr_title', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('inner_sub_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('unit_price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='content/images/')),
                ('brand_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.Brand')),
                ('subcategory_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Cat_Attr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_type', models.CharField(max_length=250)),
                ('int_value', models.IntegerField(blank=True, null=True)),
                ('text_value', models.TextField(blank=True, max_length=250, null=True)),
                ('bool_value', models.BooleanField(blank=True, null=True)),
                ('attr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Attribute')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Product')),
            ],
        ),
        migrations.AddField(
            model_name='brand',
            name='subcategory_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.SubCategory'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='subcategory_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.SubCategory'),
        ),
    ]