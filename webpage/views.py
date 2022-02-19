from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from webpage.models import Client,Contact
from webpage.forms import ClientForm
# Create your views here.

class getList(ListView): 
    model = Client

class getDetail(DetailView): 
    model = Client

'''class insert(SuccessMessageMixin, CreateView): 
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('read')
    success_message = "Product successfully created!"

class update(SuccessMessageMixin, UpdateView): 
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('read')
    success_message = "Product successfully updated!"

class delete(SuccessMessageMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('read')
    success_message = "Product successfully deleted!"
'''