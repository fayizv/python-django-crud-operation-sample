# Generated by Django 4.0.6 on 2022-07-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image_alter_product_spech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='spech',
            field=models.CharField(max_length=255),
        ),
    ]
