# Generated by Django 4.1.2 on 2022-11-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]