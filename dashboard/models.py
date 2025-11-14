
from django.db import models
from django.contrib.auth.models import User

class OrderQueue(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('done', 'Закрыта'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    initiator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='initiated_orders')
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='executed_orders', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    sla_deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} – {self.title}"

class KPIRecord(models.Model):
    metric = models.CharField(max_length=100)
    value = models.FloatField()
    timestamp = models.DateTimeField()
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.metric} {self.timestamp:%Y-%m-%d}"

class Incident(models.Model):
    CRIT_CHOICES = [
        ('low', 'Низкая'),
        ('medium', 'Средняя'),
        ('high', 'Высокая'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)
    criticality = models.CharField(max_length=20, choices=CRIT_CHOICES, default='medium')
    detected_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True, blank=True)
    related_order = models.ForeignKey(OrderQueue, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Shift(models.Model):
    SHIFT_CHOICES = [
        ('day', 'День'),
        ('night', 'Ночь'),
    ]
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    comment = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employee} {self.date} {self.shift}"

class Report(models.Model):
    REPORT_TYPES = [
        ('monthly', 'Месячный отчёт'),
        ('weekly', 'Недельный отчёт'),
        ('daily', 'Дневной отчёт'),
    ]
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    period_from = models.DateField()
    period_to = models.DateField()
    file = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_report_type_display()} {self.period_from}–{self.period_to}"

class Document(models.Model):
    ACCESS_CHOICES = [
        ('public', 'Публичный'),
        ('client', 'Клиенты'),
        ('internal', 'Внутренний'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='docs/')
    access = models.CharField(max_length=20, choices=ACCESS_CHOICES, default='public')

    def __str__(self):
        return self.title
