# Generated by Django 3.2.7 on 2022-01-01 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220101_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_hover',
        ),
    ]