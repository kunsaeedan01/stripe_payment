# Generated by Django 4.1.5 on 2023-02-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_description_item_name_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]