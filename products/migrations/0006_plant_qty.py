# Generated by Django 3.1.7 on 2021-05-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210506_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='qty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]