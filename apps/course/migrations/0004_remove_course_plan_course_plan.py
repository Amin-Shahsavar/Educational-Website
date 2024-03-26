# Generated by Django 4.2.9 on 2024-03-05 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_plan_dollar_price_and_more'),
        ('course', '0003_alter_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='plan',
        ),
        migrations.AddField(
            model_name='course',
            name='plan',
            field=models.ManyToManyField(blank=True, to='plan.plan', verbose_name='plans'),
        ),
    ]
