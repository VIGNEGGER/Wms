# Generated by Django 5.2.1 on 2025-06-02 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_supplier_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
