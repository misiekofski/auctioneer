# Generated by Django 4.2.1 on 2023-06-22 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_lot_buyer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lot',
            options={'ordering': ['-auction_date', 'endtime'], 'verbose_name_plural': 'Lots'},
        ),
    ]