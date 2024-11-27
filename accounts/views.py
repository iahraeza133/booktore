from django.shortcuts import render
from django.views import generic
from core.forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignupView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['CRISPY_TEMPLATE_PACK'] = 'bootstrap4'  # Dynamically set the template pack
    #     return context