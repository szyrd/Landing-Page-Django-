# Generated by Django 4.1.2 on 2022-10-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothrepair', '0004_priceinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceinfo',
            name='priceDescrip',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
