# Generated by Django 3.2.6 on 2021-12-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0013_alter_file_mainurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='mainurl',
            field=models.CharField(max_length=1000),
        ),
    ]
