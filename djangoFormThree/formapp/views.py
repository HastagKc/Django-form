from django.shortcuts import render
from .forms import ContactForm


# create view

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subscribe = form.cleaned_data['subscribe']
            preferred_contact_time = form.cleaned_data['preferred_contact_time']
            birthday = form.cleaned_data['birthday']
            # Save or send the data
            return render(request, 'contact_success.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'formapp/contact_form.html', {'form': form})
