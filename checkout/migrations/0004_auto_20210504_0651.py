# Generated by Django 3.1.7 on 2021-05-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210504_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
