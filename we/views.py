from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'company/home.html')

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report_obj = ReportModel.objects.create()
            cd = form.cleaned_data
            report_obj.name = cd['name']
            report_obj.email = cd['email']
            report_obj.subject = cd['subject']
            report_obj.message = cd['message']
            report_obj.save()

            return redirect('we:report')
        else:
            messages.warning(request, "Wrong info. Check teh form please!")
    else:
        form = ReportForm()

    return render(request, 'forms/report.html', {"form" : form})