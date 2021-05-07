# Generated by Django 3.2 on 2021-04-28 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GopY',
            fields=[
                ('magopy', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tenkh', models.CharField(max_length=100)),
                ('noi_dung', models.TextField(default='')),
                ('makh', models.ForeignKey(db_column='makh', on_delete=django.db.models.deletion.CASCADE, to='customer.khachhang')),
            ],
            options={
                'db_table': 'gop_y',
            },
        ),
    ]