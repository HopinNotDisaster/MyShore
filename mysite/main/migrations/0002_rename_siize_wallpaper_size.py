# Generated by Django 5.0.4 on 2024-04-16 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallpaper',
            old_name='siize',
            new_name='size',
        ),
    ]
