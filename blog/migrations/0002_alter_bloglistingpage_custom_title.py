# Generated by Django 3.2.7 on 2021-10-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglistingpage',
            name='custom_title',
            field=models.CharField(help_text='Overwrites the default title', max_length=100),
        ),
    ]
