# Generated by Django 3.2 on 2023-05-25 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_alter_lotimage_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]
