# Generated by Django 4.0b1 on 2021-11-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='depth',
            field=models.IntegerField(),
        ),
    ]
