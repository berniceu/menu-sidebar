from django.contrib import admin
from .models import Overview, ClaimsManagement, EventsSubmission, IncidentTracking, PatientRecord, PatientRelation, Message, QualityManagement,ReportsAnalytic, WorkersCompensation, User

admin.site.register(Overview)
admin.site.register(ClaimsManagement)
admin.site.register(EventsSubmission)
admin.site.register(IncidentTracking)
admin.site.register(PatientRecord)
admin.site.register(PatientRelation)
admin.site.register(Message)
admin.site.register(QualityManagement)
admin.site.register(ReportsAnalytic)
admin.site.register(WorkersCompensation)
admin.site.register(User)