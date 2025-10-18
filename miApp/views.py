from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
"""
def details_view(request, id):
    date = request.GET.get('date', 'Not provided')
    context = {'id': id, 'date': date, 'type': 'Details'}
    return render(request, 'display.html', context)

def summary_view(request, id):
    month = request.GET.get('month', 'Not provided')
    context = {'id': id, 'date': month, 'type': 'Summary'}
    return render(request, 'display.html', context)

def report_view(request, id):
    year = request.GET.get('year', 'Not provided')
    context = {'id': id, 'date': year, 'type': 'Report'}
    return render(request, 'display.html', context)
"""

def details_view(request, nombreparam):
    parametro1=request.GET.get('parametroDeConsulta1', 'Not provided')
    parametroN=request.GET.get('parametroDeConsultaN', 'Not provided')
    context = {'idEnDetails': nombreparam, 'parametroConsulta1': parametro1, 'parametroConsultaN': parametroN, 'type': 'Details'}
    return render(request, 'display.html', context)

def formEnvioParamRutaYconsulta(request):
  	return render(request, 'paramRutaYconsulta.html')

def vistaHome(request):
  	return render(request, 'plantillaHome.html')

