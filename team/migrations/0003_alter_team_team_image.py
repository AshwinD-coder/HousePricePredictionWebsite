# Generated by Django 4.1.7 on 2023-06-17 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_remove_team_team_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_image',
            field=models.ImageField(upload_to='../static/img'),
        ),
    ]