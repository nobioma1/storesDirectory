# Generated by Django 2.1.3 on 2018-11-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_store_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='stars',
            field=models.IntegerField(default=1, max_length=5),
        ),
    ]
