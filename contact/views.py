from django.shortcuts import render
from django.contrib import messages
from .models import ContactForm
from .forms import ContactForm


def contact(request):

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, 
                messages.SUCCESS,
                "Message received. We will respond as soon as possible."
                )

    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form,
         },
    )
