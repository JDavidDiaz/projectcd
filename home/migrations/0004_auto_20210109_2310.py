# Generated by Django 3.1.1 on 2021-01-09 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='download',
            new_name='file',
        ),
    ]
