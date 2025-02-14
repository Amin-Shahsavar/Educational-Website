# Generated by Django 4.2.9 on 2024-03-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='dollar_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='dollar price'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='dollar_price_discount',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='dollar price discount'),
        ),
    ]
