# Generated by Django 5.0.1 on 2024-01-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='React',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
