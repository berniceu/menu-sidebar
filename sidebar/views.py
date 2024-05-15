from django.shortcuts import render
from rest_framework.exceptions import NotFound, APIException, NotAuthenticated
from .models import  Overview, PatientRecords, Message, ClaimsManagement, EventsSubmission, IncidentTracking, PatientRelations, ReportsAnalytics, WorkersCompensation, QualityManagement 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialize import OverviewSerializer, PatientRecordsSerializer, ClaimsManagementSerializer, EventsSubmissionSerializer, IncidentTrackingSerializer, MessageSerializer, PatientRelationsSerializer, ReportsAnalyticsSerializer, QualityManagementSerializer, WorkersCompensationSerializer

from django.http import HttpResponse

@api_view(['GET'])
def overviewView(request):
    if not request.user.is_authenticated:
        raise NotAuthenticated('User not authenticated')
    try:
        overview_data = Overview.objects.all()
        serializer = OverviewSerializer(overview_data, many=True)
        return Response(serializer.data)
    except Overview.DoesNotExist:
        raise NotFound('Overview data not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def patientRecordsView(request):
    try:
        patient_records = PatientRecords.objects.all()
        serializer = PatientRecordsSerializer(patient_records, many=True)
        return Response(serializer.data)
    except PatientRecords.DoesNotExist:
        raise NotFound('Patient Records not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def messageViews(request):
    try:
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data)
    except Message.DoesNotExist:
        raise NotFound('Messages not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def claimsViews(request):
    try:
        claims = ClaimsManagement.objects.all()
        serializer = ClaimsManagementSerializer(claims, many=True)
        return Response(serializer.data)
    except ClaimsManagement.DoesNotExist:
        raise NotFound('Claims not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def eventsViews(request):
    try:
        events = EventsSubmission.objects.all()
        serializer = EventsSubmissionSerializer(events, many=True)
        return Response(serializer.data)
    except EventsSubmission.DoesNotExist:
        raise NotFound('Events not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def incidentView(request):
    try:
        incident = IncidentTracking.objects.all()
        serializer = IncidentTrackingSerializer(incident, many=True)
        return Response(serializer.data)
    except IncidentTracking.DoesNotExist:
        raise NotFound('Incidents not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))


@api_view(['GET'])
def patientRelationsView(request):
    try:
        patient_relations = PatientRelations.objects.all()
        serializer = PatientRelationsSerializer(patient_relations, many=True)
        return Response(serializer.data)
    except PatientRelations.DoesNotExist:
        raise NotFound('Patient Relations not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def reportsView(request):
    try:
        reports = ReportsAnalytics.objects.all()
        serializer = ReportsAnalyticsSerializer(reports, many=True)
        return Response(serializer.data)
    except ReportsAnalytics.DoesNotExist:
        raise NotFound('Report analytics not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def WorkersCompensationView(request):
    try:
        workers_compensation = WorkersCompensation.objects.all()
        serializer = WorkersCompensationSerializer(workers_compensation, many=True)
        return Response(serializer.data)
    except WorkersCompensation.DoesNotExist:
        raise NotFound('Workers Compensation not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def QualityManagementView(request):
    try:
        quality_management = QualityManagement.objects.all()
        serializer = QualityManagementSerializer(quality_management, many=True)
        return Response(serializer.data)
    except QualityManagement.DoesNotExist:
        raise NotFound('Events not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

def sidebarView(request):
    return render(request, 'sidebar.html')

def homepage(request):
    return HttpResponse('<h1>Welcome to the homepage!</h1>')