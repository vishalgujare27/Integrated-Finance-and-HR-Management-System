# Generated by Django 5.0.1 on 2024-04-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_rename_delivery_time_tc_proforma_invoce_po_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tax_invoce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PI_number', models.CharField(max_length=150)),
                ('invoice_date', models.CharField(max_length=150)),
                ('PO_number', models.CharField(max_length=150)),
                ('po_date', models.CharField(max_length=150)),
                ('customer_name', models.CharField(max_length=150)),
                ('customer_address', models.CharField(max_length=150)),
                ('customer_contact', models.CharField(max_length=150)),
                ('customer_gst', models.CharField(max_length=150)),
                ('customer_reference', models.CharField(max_length=150)),
                ('sr_no', models.CharField(max_length=150)),
                ('item_details', models.TextField()),
                ('grade', models.CharField(max_length=150)),
                ('uom', models.CharField(max_length=150)),
                ('moq', models.CharField(max_length=150)),
                ('rate', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=150)),
                ('remark', models.CharField(max_length=150)),
                ('totalAmount', models.CharField(max_length=150)),
                ('packingForwarding', models.CharField(max_length=150)),
                ('cgst', models.CharField(max_length=150)),
                ('cgst_total', models.CharField(max_length=150)),
                ('sgst', models.CharField(max_length=150)),
                ('sgst_total', models.CharField(max_length=150)),
                ('igst', models.CharField(max_length=150)),
                ('igst_total', models.CharField(max_length=150)),
                ('grand_total', models.CharField(max_length=150)),
                ('amt_in_words', models.CharField(max_length=150)),
            ],
        ),
    ]
