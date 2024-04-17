# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

from django.views.generic import (ListView,
                                  DetailView,
                                  TemplateView)


from transport.models import Fuel_mgt, Vehicle_register


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Fuel_mgt.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

class ChartView(TemplateView):
    template_name = "dashboard/dash-board.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_registrations'] = Vehicle_register.objects.count()
        context['total_operational'] = Vehicle_register.objects.filter(operational_status='operational').count()
        context['total_grounded'] = Vehicle_register.objects.filter(operational_status='grounded').count()
        return context