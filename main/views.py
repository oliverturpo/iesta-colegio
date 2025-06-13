from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Para Servirle Mi King 👑")

def status(request):
    import django
    from datetime import datetime
    
    html = f"""
    <h1>🚀 Sistema IESTA - Estado del Servidor</h1>
    <ul>
        <li>✅ Django Version: {django.get_version()}</li>
        <li>✅ Servidor funcionando correctamente</li>
        <li>✅ Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</li>
        <li>✅ Proyecto: Sistema de Control de Asistencia</li>
    </ul>
    <p><a href="/">← Volver al inicio</a></p>
    """
    return HttpResponse(html)