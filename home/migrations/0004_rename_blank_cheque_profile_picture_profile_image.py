# Generated by Django 3.2.6 on 2023-07-31 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_company_profile_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_picture',
            old_name='blank_cheque',
            new_name='profile_image',
        ),
    ]
