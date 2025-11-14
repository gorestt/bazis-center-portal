
from django import forms
from .models import OrderQueue, Document, Report

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderQueue
        fields = ['title', 'description', 'priority', 'status', 'executor']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'slug', 'description', 'access', 'file']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_type', 'period_from', 'period_to']
