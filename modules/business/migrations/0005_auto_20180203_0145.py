# Generated by Django 2.0.1 on 2018-02-03 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20180130_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b2cprofile',
            old_name='image_file',
            new_name='image',
        ),
    ]