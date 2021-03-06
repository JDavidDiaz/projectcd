# Generated by Django 3.1.1 on 2021-01-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_delete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('uploaddate', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='FileU',
        ),
    ]
