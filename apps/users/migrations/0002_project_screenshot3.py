# Generated by Django 3.2.5 on 2021-07-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='screenshot3',
            field=models.ImageField(null=True, upload_to='projects'),
        ),
    ]
