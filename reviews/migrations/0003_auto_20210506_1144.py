# Generated by Django 3.1.7 on 2021-05-06 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210506_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='order_id',
            new_name='order',
        ),
    ]