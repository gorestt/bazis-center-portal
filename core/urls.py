
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('public-queue/', views.public_queue, name='public_queue'),
    path('public-kpi/', views.public_kpi, name='public_kpi'),
    path('public-incidents/', views.public_incidents, name='public_incidents'),
    path('public-shifts/', views.public_shifts, name='public_shifts'),
    path('public-reports/', views.public_reports, name='public_reports'),
    path('docs/', views.docs_public, name='docs_public'),
    path('faq/', views.faq, name='faq'),
    path('services/', views.services, name='services'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
