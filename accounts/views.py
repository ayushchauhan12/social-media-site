from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class Signup(CreateView):
    form_class=forms.Usercreateform
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
