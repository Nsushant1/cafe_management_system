from django.shortcuts import render, get_object_or_404, redirect
from .models import InventoryItem
from .forms import InventoryItemForm

def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

def inventory_create(request):
    form = InventoryItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_form.html', {'form': form})

def inventory_update(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    form = InventoryItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_form.html', {'form': form})

def inventory_delete(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_confirm_delete.html', {'item': item})
