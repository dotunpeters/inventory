# Generated by Django 3.1.2 on 2020-10-25 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201025_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tank',
            old_name='tanks_name',
            new_name='tank_name',
        ),
    ]
