from django.shortcuts import render

# Create your views here.

def index_view(request):
    from django import forms
    class LoginForm(forms.Form):
        usuario = forms.CharField(label='Usuario', max_length=100)

    template = "rutinas/base.html"
    context = { "form" : LoginForm() }
    return render( request, template, context )