# Generated by Django 5.0.6 on 2024-05-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0005_user_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=70),
        ),
    ]
