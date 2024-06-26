# Generated by Django 5.0.1 on 2024-05-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customersemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='point',
            field=models.IntegerField(default=1),
        ),
    ]
