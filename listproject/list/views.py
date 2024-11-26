from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import ListItem
from .serializers import ListItemSerializer
from django.contrib import messages

from django.http import JsonResponse

from django.http import HttpResponse


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

def list_view(request):
    items = ListItem.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ListItem.objects.create(title=title, description=description)
        messages.success(request, 'Item added successfully!')
    return redirect('list_view')

def delete_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    item.delete()
    messages.success(request, 'Item deleted successfully!')
    return redirect('list_view')

def complete_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    item.completed = not item.completed
    item.save()
    messages.success(request, 'Item status updated!')
    return redirect('list_view')



from django.http import JsonResponse

# def health_check(request):
#     return JsonResponse({'status': 'healthy'})
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)


# In your Django app views.py


def favicon(request):
    return HttpResponse(status=204)  # No content
