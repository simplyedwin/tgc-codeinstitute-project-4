# Generated by Django 3.1.7 on 2021-05-13 11:39

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userinfo_favourite_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, validators=[users.models.age_check]),
        ),
    ]
