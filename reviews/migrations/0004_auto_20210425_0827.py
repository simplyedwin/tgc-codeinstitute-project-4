# Generated by Django 3.1.7 on 2021-04-25 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20210425_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='owner',
            new_name='reviewed_by',
        ),
    ]