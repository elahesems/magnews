# Generated by Django 3.2.5 on 2021-07-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]