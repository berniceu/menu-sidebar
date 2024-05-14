from django.db import models

class Overview(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()

class PatientRecords(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    
class IncidentTracking(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class QualityManagement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class PatientRelations(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class ClaimsManagement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class WorkersCompensation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Message(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class EventsSubmission(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class ReportsAnalytics(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()