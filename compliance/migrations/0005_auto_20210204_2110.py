# Generated by Django 3.1.6 on 2021-02-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0004_auto_20210204_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='ec_sales_deadline',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='country',
            name='intrastat_deadline',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='country',
            name='vat_deadline',
            field=models.CharField(max_length=40),
        ),
    ]
