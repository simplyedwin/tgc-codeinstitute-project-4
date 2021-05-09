# Generated by Django 3.1.7 on 2021-05-09 02:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_plant_qty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('checkout', '0006_auto_20210504_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('rating', models.IntegerField()),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.order')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.plant')),
                ('reviewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
