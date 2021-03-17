# Generated by Django 3.1.7 on 2021-03-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('image_URL', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('edition', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('rating', models.FloatField()),
            ],
        ),
    ]