# Generated by Django 2.2.5 on 2021-12-29 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211228_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='accurancy',
            new_name='accuracy',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='cleanlines',
            new_name='cleanliness',
        ),
    ]