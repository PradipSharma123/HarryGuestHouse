# Generated by Django 4.0.3 on 2022-03-08 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_icon', models.CharField(max_length=25)),
                ('Service_name', models.CharField(max_length=100)),
                ('Service_desc', models.TextField()),
            ],
        ),
    ]