from django.contrib import admin
from .models import Overview, ClaimsManagement, EventsSubmission, IncidentTracking, PatientRecords, PatientRelations, Message, QualityManagement,ReportsAnalytics, WorkersCompensation

admin.site.register(Overview)
admin.site.register(ClaimsManagement)
admin.site.register(EventsSubmission)
admin.site.register(IncidentTracking)
admin.site.register(PatientRecords)
admin.site.register(PatientRelations)
admin.site.register(Message)
admin.site.register(QualityManagement)
admin.site.register(ReportsAnalytics)
admin.site.register(WorkersCompensation)