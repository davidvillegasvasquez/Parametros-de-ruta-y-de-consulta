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

def vistaParamDeRutaYConsultaVariables(request, parametroUnicoDeRuta):
    #parametroDeRuta=request.GET.get('parametroDeRuta', 'Not provided')
    parametro1=request.GET.get('parametroDeConsulta1', 'Not provided')
    parametroN=request.GET.get('parametroDeConsultaN', 'Not provided')
    parametroDelTipo=request.GET.get('tipo', 'Not provided')
    context = {'parametroDeRuta': parametroUnicoDeRuta, 'parametroConsulta1': parametro1, 'parametroConsultaN': parametroN, 'tipoDado': parametroDelTipo}
    return render(request, 'plantillaComunDeResultado.html', context)

def formEnvioParamRutaYconsulta(request):
  	return render(request, 'formularioEnvio.html')

def vistaHome(request):
  	return render(request, 'plantillaHome.html')

"""
Por que no puedo meter enteros negativos en el parametro de ruta url:
El error ocurre porque el patrón de ruta (path) por defecto de Django no está configurado para reconocer el signo negativo (-) en los parámetros de la URL. Para solucionar esto, debes utilizar re_path con una expresión regular que acepte números negativos, o ajustar el parámetro de ruta a un tipo de dato que pueda ser negativo. 
"""