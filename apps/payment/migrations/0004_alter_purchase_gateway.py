# Generated by Django 4.2.9 on 2024-03-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_purchase_invoice_number_alter_purchase_gateway_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='gateway',
            field=models.CharField(choices=[('PAYPAL', 'Paypal'), ('PARSIAN', 'Parsian')], default='PARSIAN', verbose_name='gateway'),
        ),
    ]
