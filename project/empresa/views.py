from django.shortcuts import render, redirect

from . import models, forms

def home (request):
    query = models.Areas.objects.all()
    contexto = {"areas": query}
    return render(request, "empresa/index.html", context=contexto)

def empleado_create (request):
    if request.method == "POST":
        form = forms.EmpleadosCreateForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect("empresa:empleados")
        except ValueError:
               ...
    else:  # request.method == "GET"
        form = forms.EmpleadosCreateForm()
    return render(request, "empresa/empleado_create.html", context={"form": form})

def empleados(request):
    query = models.Empleados.objects.all()
    contexto = {"empleados": query}
    return render(request, "empresa/empleados.html", context=contexto)

def buscar_empleado(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        query = models.Empleados.objects.filter(documento__icontains=consulta)
        return render(request, "empresa/buscar_empleado.html", {"resultados": query})
    return render(request, "empresa/buscar_empleado.html")