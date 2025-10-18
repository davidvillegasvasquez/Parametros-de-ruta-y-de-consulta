from django.urls import path
from . import views
"""
urlpatterns = [
  	path('', views.index_view, name='index'),
    path('detalles/<int:id>/', views.details_view, name='details'),
    path('resumen/<int:id>/', views.summary_view, name='summary'),
    path('reporte/<int:id>/', views.report_view, name='report'),
]

Estas mapeadores de url eran para cuando usamos el enfoque de usar parámetros de ruta constantes en la etiqueta de plantilla url, hipervinculados en la plantilla:
     
        <li><a href="{% url 'details' id=1 %}?date=2024-01-01">View Details for ID 1</a></li>
        <li><a href="{% url 'summary' id=2 %}?month=August">View Summary for ID 2</a></li>
        <li><a href="{% url 'report' id=3 %}?year=2023">View Report for ID 3</a></li>

Aquí podemos sustituir id=1, id=2 e id=3 como literales 1,2 y 3, respectivamente.

"""

urlpatterns = [
  	path('', views.vistaHome, name='home'),
    path('envíoParamsRutaYdeConsulta/', views.formEnvioParamRutaYconsulta, name='formParamRutaYconsulta'), path('envioParamRutaYConsulta/<int:nombreparam>/', views.details_view, name='paramRutaYconsulta'),
]