# Generated by Django 3.2.4 on 2021-07-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabanBoardApp', '0003_auto_20210710_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.IntegerField()),
                ('taskname', models.CharField(default='null', max_length=20)),
                ('taskid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'ProgressInfo',
            },
        ),
    ]
