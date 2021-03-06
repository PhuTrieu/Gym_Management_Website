# Generated by Django 3.1.7 on 2021-04-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ds_phonggym',
            fields=[
                ('mapg', models.AutoField(primary_key=True, serialize=False)),
                ('sdt', models.IntegerField()),
                ('gmail', models.CharField(max_length=100)),
                ('diachi', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ds_phonggym',
            },
        ),
        migrations.CreateModel(
            name='slide_quangcao',
            fields=[
                ('maqc', models.AutoField(primary_key=True, serialize=False)),
                ('tieu_de', models.CharField(max_length=100)),
                ('hinh', models.ImageField(upload_to='slide_quangcao_imgs/')),
            ],
            options={
                'db_table': 'slide_quangcao',
            },
        ),
    ]
