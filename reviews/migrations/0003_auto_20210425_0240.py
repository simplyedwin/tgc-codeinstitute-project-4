# Generated by Django 3.1.7 on 2021-04-25 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210425_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
