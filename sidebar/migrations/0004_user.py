# Generated by Django 5.0.6 on 2024-05-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0003_rename_patientrecords_patientrecord_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
    ]
