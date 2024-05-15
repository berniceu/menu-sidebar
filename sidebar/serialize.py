from rest_framework import serializers
from .models import Overview, ClaimsManagement, EventsSubmission, IncidentTracking, PatientRecord, PatientRelation, Message, QualityManagement,ReportsAnalytic, WorkersCompensation, User

class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        overview_model = Overview
        fields = '__all__'

class ClaimsManagementSerializer(serializers.ModelSerializer):
    class Meta:
        claims_management_model = ClaimsManagement
        fields = '__all__'

class EventsSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        events_submission_model = EventsSubmission
        fields = '__all__'

class IncidentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        incident_tracking_model = IncidentTracking
        fields = '__all__'

class PatientRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        patient_record_model = PatientRecord
        fields = '__all__'

class PatientRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        patient_relation_model = PatientRelation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        message_model = Message
        fields = '__all__'

class QualityManagementSerializer(serializers.ModelSerializer):
    class Meta:
        quality_management_model = QualityManagement
        fields = '__all__'

class ReportsAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        reports_analytic_model = ReportsAnalytic
        fields = '__all__'

class WorkersCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        workers_compensation_model = WorkersCompensation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'