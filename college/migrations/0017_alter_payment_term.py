# Generated by Django 5.0b1 on 2024-01-09 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0016_payment_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.term'),
        ),
    ]
