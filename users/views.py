from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from .forms import registrationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        messages.error(request, "U R Already in!")
        form = registrationForm

    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('/')
        else:
            for error in list(form.errors.values()):
                print((request, error))

    else:
        form = registrationForm

    context = {
        'form' : form
    }
    return render(request, 'forms/registration.html', context)