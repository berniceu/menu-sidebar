from rest_framework import serializers
from .models import Overview, ClaimsManagement, EventsSubmission, IncidentTracking, PatientRecords, PatientRelations, Message, QualityManagement,ReportsAnalytics, WorkersCompensation

class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = '__all__'

class ClaimsManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimsManagement
        fields = '__all__'

class EventsSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsSubmission
        fields = '__all__'

class IncidentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentTracking
        fields = '__all__'

class PatientRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecords
        fields = '__all__'

class PatientRelationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRelations
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class QualityManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityManagement
        fields = '__all__'

class ReportsAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportsAnalytics
        fields = '__all__'

class WorkersCompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkersCompensation
        fields = '__all__'