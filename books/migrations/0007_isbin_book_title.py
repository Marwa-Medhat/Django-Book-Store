# Generated by Django 3.2 on 2021-04-23 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210423_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='isbin',
            name='book_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
