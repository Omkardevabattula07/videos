# Generated by Django 4.2.13 on 2024-07-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='uploaded_at',
            field=models.DateTimeField(),
        ),
    ]
