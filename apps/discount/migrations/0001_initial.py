# Generated by Django 4.2.9 on 2024-02-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='title')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('max_use', models.PositiveIntegerField(blank=True, null=True, verbose_name='max use')),
                ('discount_percent', models.PositiveIntegerField(blank=True, null=True, verbose_name='discount percent')),
                ('toman_discount_amount', models.PositiveIntegerField(verbose_name='toman discount amount')),
                ('dollar_discount_amount', models.PositiveIntegerField(verbose_name='dollar discount amount')),
            ],
        ),
    ]
