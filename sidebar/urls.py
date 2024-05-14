from django.urls import path
from . import views

urlpatterns = [
    path('overview/', views.overviewView),
    path('patientrecords/', views.patientRecordsView),
    path('messages/', views.messageViews),
    path('claims/', views.claimsViews),
    path('events/', views.eventsViews),
    path('incident/', views.incidentView),
    path('patientrelations/', views.patientRelationsView),
    path('reports/', views.reportsView),
    path('workerscompensation/', views.WorkersCompensationView),
    path('qualitymanagement/', views.QualityManagementView),
    path('', views.sidebarView, name='sidebar'),

    
]