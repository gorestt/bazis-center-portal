
from django.shortcuts import render
from django.utils import timezone
from dashboard.models import Document, OrderQueue, KPIRecord, Incident, Shift, Report
from .models import ContactMessage

def index(request):
    open_orders = OrderQueue.objects.filter(status__in=['new','in_progress']).count()
    kpi_sample = KPIRecord.objects.order_by('-timestamp')[:5]
    return render(request, 'core/index.html', {
        'open_orders': open_orders,
        'kpi_sample': kpi_sample,
    })

def public_queue(request):
    orders = OrderQueue.objects.order_by('-created_at')[:50]
    return render(request, 'core/public_queue.html', {'orders': orders})

def public_kpi(request):
    last_7 = timezone.now() - timezone.timedelta(days=7)
    kpi = KPIRecord.objects.filter(timestamp__gte=last_7)
    return render(request, 'core/public_kpi.html', {'kpi': kpi})

def public_incidents(request):
    incidents = Incident.objects.order_by('-detected_at')[:50]
    return render(request, 'core/public_incidents.html', {'incidents': incidents})

def public_shifts(request):
    shifts = Shift.objects.select_related('employee').order_by('date')[:60]
    return render(request, 'core/public_shifts.html', {'shifts': shifts})

def public_reports(request):
    reports = Report.objects.order_by('-created_at')[:20]
    return render(request, 'core/public_reports.html', {'reports': reports})

def docs_public(request):
    docs = Document.objects.filter(access='public')
    return render(request, 'core/docs_public.html', {'docs': docs})

def faq(request):
    return render(request, 'core/faq.html')

def services(request):
    return render(request, 'core/services.html')

def news(request):
    return render(request, 'core/news.html')

def about(request):
    return render(request, 'core/about.html')

def contacts(request):
    success = False
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            message=request.POST.get('message', ''),
        )
        success = True
    return render(request, 'core/contacts.html', {'success': success})
