from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import procedimientos


# Create your views here.
def inicio(request):
            return render(request, 'app/index.html')

#carlita
def procedimientos(request):
    data = {
        'form': ProcedimientosForm()
    }
    
    if request.method == 'POST':
        form = ProcedimientosForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'app/agradecimiento.html', {'nombre': nombre, 'celular': celular, 'grado': grado})
    else:
        form = MatriculaForm()

    return render(request, 'app/contacme.html', {'form': form})
