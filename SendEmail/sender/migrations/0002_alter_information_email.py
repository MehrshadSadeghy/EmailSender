# Generated by Django 4.2.6 on 2023-12-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
