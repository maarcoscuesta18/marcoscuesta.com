from math import trunc
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from webpage.forms import ContactForm,PasswordGeneratorForm

import string,secrets

def handler404(request, exception, template_name="common/404.html"):
    response = render(request,template_name)
    response.status_code = 404
    return response


def handler500(request,template_name="common/500.html"):
    response = render(request,template_name)
    response.status_code = 500
    return response

def index(request):
    message_sended=1
    form = ContactForm()
    context = {'form': form,
        'message_sended':message_sended}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            email_subject = f'{form.cleaned_data["subject"]}'
            email_message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email_address"]}\nMessage: {form.cleaned_data["message"]}'
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, settings.ADMIN_EMAIL)
            form = ContactForm()
            message_sended=0
            return HttpResponseRedirect("/",context)
        else:
            form = ContactForm()
            message_sended=1  
            return HttpResponseRedirect("/",context)        
    return render(request,'index.html',context)


def passwordgenerator(request):
    thepass = ""
    passwordform = PasswordGeneratorForm()
    context = {'password': thepass,
    'passwordform': passwordform}
    if request.method == 'POST':
        passwordform = PasswordGeneratorForm(request.POST)
        if passwordform.is_valid():
            passwordform.save()
            
            passlength = passwordform.cleaned_data["length"]
            passlength = int(passlength)

            printable = f'{string.ascii_letters}{string.digits}{string.punctuation}'
            thepass = ''.join((secrets.choice(printable) for i in range(passlength)))
            context = {'password': thepass,
               'passwordform': passwordform}
            return render(request,"passwordgen.html",context)
        else:
            passwordform = PasswordGeneratorForm()
            return HttpResponseRedirect("passgen")  
    return render(request, 'passwordgen.html', context)

