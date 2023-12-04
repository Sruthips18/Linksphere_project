from django.shortcuts import render,redirect
from django.views.generic import View,FormView,CreateView
from socialapp.forms import RegistrationForm
from django.urls import reverse

class SignUpView(CreateView):
    template_name='register.html'
    form_class=RegistrationForm

    def get_success_url(self):
        return reverse('signup')

   
