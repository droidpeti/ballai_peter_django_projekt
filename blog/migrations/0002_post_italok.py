# Generated by Django 3.2.16 on 2022-12-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='italok',
            field=models.TextField(null=True),
        ),
    ]
