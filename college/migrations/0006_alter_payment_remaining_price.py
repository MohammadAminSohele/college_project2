# Generated by Django 5.0b1 on 2024-01-05 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_alter_payment_account_alter_payment_remaining_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='remaining_price',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]