# Generated by Django 5.0.6 on 2024-05-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0006_alter_user_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]
