from django.db import models

class Overview(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class PatientRecord(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()

    def __str__(self):
        return self.patient_name
    
class IncidentTracking(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class QualityManagement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class PatientRelation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class ClaimsManagement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class WorkersCompensation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class EventsSubmission(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class ReportsAnalytic(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class User(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=70, unique=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'