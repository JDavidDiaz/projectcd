# Generated by Django 3.1.1 on 2021-01-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_boxuser_folder_newfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='newfile',
            name='folder',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='file',
            name='filetype',
        ),
        migrations.AlterField(
            model_name='file',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='file',
            name='uploaddate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='BoxUser',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
        migrations.DeleteModel(
            name='NewFile',
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
