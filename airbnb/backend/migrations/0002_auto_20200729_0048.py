# Generated by Django 3.0.8 on 2020-07-28 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airbnb',
            old_name='name',
            new_name='title',
        ),
    ]