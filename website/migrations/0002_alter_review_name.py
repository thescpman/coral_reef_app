# Generated by Django 4.2.5 on 2023-09-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.TextField(max_length=500),
        ),
    ]
