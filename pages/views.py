from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Store, Inbox
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class IndexListView(ListView):
    model = Store
    template_name = 'pages/index.html'

class StoreDetailView(DetailView):
    model = Store
    template_name = 'pages/storedetail.html'

class StoreCreateView(CreateView):
    model = Store
    template_name = 'pages/newstore.html'
    fields = '__all__'

class StoreUpdateView(UpdateView):
    model = Store
    fields = ['storename', 'storeaddress', 'storedetails', 'storeowner', 'contact', 'stars']
    template_name = 'pages/editstore.html'

class StoreDeleteView(DeleteView):
    model = Store
    template_name = 'pages/deletestore.html'
    success_url = reverse_lazy('index')

class ContactCreateView(CreateView):
    model = Inbox
    template_name = 'pages/contact.html'
    fields = ['name', 'contact', 'message']
