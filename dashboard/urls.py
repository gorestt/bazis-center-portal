
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.home, name='home'),
    path('queue/', views.queue_list, name='queue_list'),
    path('queue/create/', views.queue_create, name='queue_create'),
    path('queue/<int:pk>/', views.queue_detail, name='queue_detail'),
    path('queue/<int:pk>/edit/', views.queue_edit, name='queue_edit'),
    path('kpi/', views.kpi_dashboard, name='kpi_dashboard'),
    path('incidents/', views.incidents_list, name='incidents_list'),
    path('shifts/', views.shifts_list, name='shifts_list'),
    path('reports/', views.reports_panel, name='reports_panel'),
    path('reports/<int:pk>/download/', views.report_download, name='report_download'),
    path('docs-manage/', views.docs_manage, name='docs_manage'),
    path('client/home/', views.client_home, name='client_home'),
    # API
    path('api/queue/', views.queue_api, name='queue_api'),
    path('api/kpi/', views.kpi_api, name='kpi_api'),
]
