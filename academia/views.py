from django.shortcuts import render
from .models import Evaluacion

# Create your views here.
def index(request):
    return render(request, "index.html",{
        "alumnos": Evaluacion.objects.all()
    })

def grabar_datos(request):
    for alumno in Evaluacion.objects.all():
        if request.POST[f"{alumno.id}"]:
            alumno.nota = request.POST[f"{alumno.id}"]
            alumno.save()
    
    return render(request, "index.html", {
        "alumnos": Evaluacion.objects.all()
    })