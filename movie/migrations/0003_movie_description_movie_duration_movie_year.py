# Generated by Django 4.2.4 on 2023-09-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
