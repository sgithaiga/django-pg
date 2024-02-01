# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

from django.views.generic import (ListView,
                                  DetailView,
                                  TemplateView)


from transport.models import Fuel_mgt


def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

def pivot_data(request):
    dataset = Fuel_mgt.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

class ChartView(TemplateView):
    template_name = "dashboard/dash-board.html"