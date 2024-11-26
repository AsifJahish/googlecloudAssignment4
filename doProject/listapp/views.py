

import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import ListItem
from .forms import ListItemForm

def index(request):
    items = ListItem.objects.all()
    return render(request, 'listapp/index.html', {'items': items})



def add_item(request):
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            new_item = form.save()

            # Prepare data for the confirmation email using 'title' instead of 'name'
            email_data = {
                'item_name': new_item.title,  # Corrected to use 'title'
                'item_description': new_item.description,  # This is fine
                'to_email': 'asifjahish2022@gmail.com',  # Replace with your email
            }

            # Make a POST request to the Cloud Function for sending the email
            try:
                response = requests.post(
                    'https://us-central1-midproject-438621.cloudfunctions.net/send_email',
                    json=email_data
                )
                response.raise_for_status()  # Raise an error for bad responses
                print('Confirmation email sent successfully.')
            except requests.exceptions.RequestException as e:
                print('Failed to send confirmation email:', e)
                # Optionally handle error, e.g., set a message to notify the user

            return redirect('index')
    else:
        form = ListItemForm()
    return render(request, 'listapp/add_item.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    if request.method == 'POST':
        form = ListItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ListItemForm(instance=item)
    return render(request, 'listapp/edit_item.html', {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'listapp/delete_item.html', {'item': item})
