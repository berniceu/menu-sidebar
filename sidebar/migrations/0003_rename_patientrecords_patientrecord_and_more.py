# Generated by Django 5.0.6 on 2024-05-15 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sidebar', '0002_alter_overview_published_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PatientRecords',
            new_name='PatientRecord',
        ),
        migrations.RenameModel(
            old_name='PatientRelations',
            new_name='PatientRelation',
        ),
        migrations.RenameModel(
            old_name='ReportsAnalytics',
            new_name='ReportsAnalytic',
        ),
    ]
