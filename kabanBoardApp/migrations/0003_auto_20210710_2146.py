# Generated by Django 3.2.4 on 2021-07-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabanBoardApp', '0002_alter_cardinfo_cardno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardinfo',
            name='taskn',
        ),
        migrations.AddField(
            model_name='cardinfo',
            name='taskname',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
