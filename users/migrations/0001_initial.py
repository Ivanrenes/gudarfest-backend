# Generated by Django 3.2.5 on 2021-07-22 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='people/pictures')),
            ],
        ),
    ]