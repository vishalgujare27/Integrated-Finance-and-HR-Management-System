# Generated by Django 3.2.6 on 2023-09-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20230911_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
