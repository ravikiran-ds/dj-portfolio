# Generated by Django 2.2.5 on 2020-12-30 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0002_auto_20201230_1942'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages2',
            new_name='Message',
        ),
    ]