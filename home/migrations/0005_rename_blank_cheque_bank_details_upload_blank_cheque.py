# Generated by Django 3.2.6 on 2023-08-02 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_blank_cheque_profile_picture_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank_details',
            old_name='blank_cheque',
            new_name='upload_blank_cheque',
        ),
    ]
