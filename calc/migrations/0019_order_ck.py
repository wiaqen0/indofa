# Generated by Django 4.0.3 on 2023-05-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0018_order_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='CK',
            field=models.BooleanField(default=True),
        ),
    ]
