from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.overview_view),
    path('patientrecords/', views.patient_records_view),
    path('messages/', views.message_views),
    path('claims/', views.claims_views),
    path('events/', views.events_views),
    path('incident/', views.incident_view),
    path('patientrelations/', views.patient_relations_view),
    path('reports/', views.reports_view),
    path('workerscompensation/', views.workers_compensation_view),
    path('qualitymanagement/', views.quality_management_view),
    path('', views.sidebar_view, name='sidebar'),
    

    
]