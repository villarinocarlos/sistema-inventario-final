from django.shortcuts import  get_object_or_404, render, redirect
from .models import Inventario
from django.contrib.auth.decorators import login_required
from .forms import AddInventarioForm, InventarioUpdateForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def inventario_lista(request):
    query = request.GET.get('q', '')
    inventarios = Inventario.objects.all()
    
    if query:
        inventarios = inventarios.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(categoria__icontains=query)
        )
    
    paginator = Paginator(inventarios, 5)  # Muestra 5 items por página.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        "title": "Lista Inventario",
        "page_obj": page_obj,
        "query": query
    }
    return render(request, "inventario/inventario_lista.html", context=context)
@login_required
def por_producto_view(request, pk):
    inventario =  get_object_or_404(Inventario, pk=pk)
    context = {

      'inventario': inventario
    }

    return render(request, "inventario/por_producto.html", context=context)

@login_required
def add_product(request):
    if request.method == "POST":
        updateForm = AddInventarioForm(data=request.POST)
        if updateForm.is_valid():
            new_inventory = updateForm.save(commit=False)
            new_inventory.ventas = float(updateForm.data['precio']) * float(updateForm.data['stock'])
            new_inventory.save()
            return redirect("inventario_lista")
    else:
        updateForm = AddInventarioForm()

    return render(request, "inventario/inventario_agregar.html", {'form': updateForm})

@login_required()
def delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    inventario.delete()
    messages.success(request, "Inventario eliminado")
    return redirect("/inventario/")

@login_required()

def update(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        updateForm = InventarioUpdateForm(request.POST, instance=inventario)
        if updateForm.is_valid():
            inventario = updateForm.save(commit=False)
            inventario.sales = float(inventario.precio) * float(inventario.stock)
            inventario.save()
            return redirect("por_producto", pk=pk)
    else:
        updateForm = InventarioUpdateForm(instance=inventario)

    return render(request, "inventario/inventario_actualizar.html", {'form': updateForm, 'inventario': inventario})