
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.template.loader import get_template
from .form import *
from homepage.form import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage



def Index(request):

    return render(request , "index.html")


# def Contact(request):
#     return render(request , "contact-form.html")


def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('contact_form.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_content': contact_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New email from dev-vansh",
                content,
                "dev-vansh" + '',
                ['vansh.bhardwaj1999@gmail.com'],
                headers={'Reply To': contact_email}
            )

            email.send()

            return redirect('success')
    return render(request, 'contact-form.html', {'form': Contact_Form})

def Success(request):
    return render(request, 'success.html')
