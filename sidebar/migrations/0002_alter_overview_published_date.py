# Generated by Django 5.0.6 on 2024-05-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overview',
            name='published_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
