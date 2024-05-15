from django.shortcuts import render
from rest_framework.exceptions import NotFound, APIException, NotAuthenticated
from .models import  Overview, PatientRecord, Message, ClaimsManagement, EventsSubmission, IncidentTracking, PatientRelation, ReportsAnalytic, WorkersCompensation, QualityManagement, User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialize import OverviewSerializer, PatientRecordsSerializer, ClaimsManagementSerializer, EventsSubmissionSerializer, IncidentTrackingSerializer, MessageSerializer, PatientRelationsSerializer, ReportsAnalyticsSerializer, QualityManagementSerializer, WorkersCompensationSerializer, UserSerializer

from django.http import HttpResponse

@api_view(['GET'])
def overview_view(request):
    if not request.user.is_authenticated:
        raise NotAuthenticated('User not authenticated')
    try:
        overview_data = Overview.objects.all()
        overview_serializer = OverviewSerializer(overview_data, many=True)
        return Response(overview_serializer.data)
    except Overview.DoesNotExist:
        raise NotFound('Overview data not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def patient_records_view(request):
    try:
        patient_records = PatientRecord.objects.all()
        patient_records_serializer = PatientRecordsSerializer(patient_records, many=True)
        return Response(patient_records_serializer.data)
    except PatientRecord.DoesNotExist:
        raise NotFound('Patient Records not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def message_views(request):
    try:
        message = Message.objects.all()
        message_serializer = MessageSerializer(message, many=True)
        return Response(message_serializer.data)
    except Message.DoesNotExist:
        raise NotFound('Messages not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def claims_views(request):
    try:
        claims = ClaimsManagement.objects.all()
        claims_serializer = ClaimsManagementSerializer(claims, many=True)
        return Response(claims_serializer.data)
    except ClaimsManagement.DoesNotExist:
        raise NotFound('Claims not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def events_views(request):
    try:
        events = EventsSubmission.objects.all()
        events_serializer = EventsSubmissionSerializer(events, many=True)
        return Response(events_serializer.data)
    except EventsSubmission.DoesNotExist:
        raise NotFound('Events not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def incident_view(request):
    try:
        incident = IncidentTracking.objects.all()
        incident_serializer = IncidentTrackingSerializer(incident, many=True)
        return Response(incident_serializer.data)
    except IncidentTracking.DoesNotExist:
        raise NotFound('Incidents not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))


@api_view(['GET'])
def patient_relations_view(request):
    try:
        patient_relations = PatientRelation.objects.all()
        patient_relations_serializer = PatientRelationsSerializer(patient_relations, many=True)
        return Response(patient_relations_serializer.data)
    except PatientRelation.DoesNotExist:
        raise NotFound('Patient Relations not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def reports_view(request):
    try:
        reports = ReportsAnalytic.objects.all()
        reports_serializer = ReportsAnalyticsSerializer(reports, many=True)
        return Response(reports_serializer.data)
    except ReportsAnalytic.DoesNotExist:
        raise NotFound('Report analytics not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def workers_compensation_view(request):
    try:
        workers_compensation = WorkersCompensation.objects.all()
        workers_compensation_serializer = WorkersCompensationSerializer(workers_compensation, many=True)
        return Response(workers_compensation_serializer.data)
    except WorkersCompensation.DoesNotExist:
        raise NotFound('Workers Compensation not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

@api_view(['GET'])
def quality_management_view(request):
    try:
        quality_management = QualityManagement.objects.all()
        quality_management_serializer = QualityManagementSerializer(quality_management, many=True)
        return Response(quality_management_serializer.data)
    except QualityManagement.DoesNotExist:
        raise NotFound('Events not found')
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))
    
@api_view(['POST', 'GET'])
def full_name_view(request):
    try:
        if request.method == 'POST':
            user_full_name = request.data.get('full_name')
            user_email = request.data.get('email')

            if not user_email:
                return Response({'error': 'Email is required'}, status=400)

            if not user_full_name:
                return Response({'error': 'Full Name is required'}, status=400)
            
            if User.objects.filter(user_email=user_email).exists():
                return Response({'error': 'User already exists'})
            
            full_name = user_full_name.split(" ")
            
            first_name = full_name[0]
            last_name = ' '.join(full_name[1:])

            user = User(first_name=first_name, last_name=last_name, user_email=user_email)
            user.save()
            user_serializer = UserSerializer(user)

            return Response({"message": "subscribed successfully", "user": user_serializer.data}, status=201)
        
        if request.method == 'GET':
            subscribed_users = User.objects.all()
            subscribed_users_serializer = UserSerializer(subscribed_users, many=True)
            return Response(subscribed_users_serializer.data)

        
    except Exception as e:
        raise APIException('Server error: {}'.format(str(e)))

def sidebar_view(request):
    return render(request, 'sidebar.html')

def homepage(request):
    return HttpResponse('<h1>Welcome to the homepage!</h1>')