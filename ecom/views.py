from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from ecom.forms import SignUpForm


def sign_up(request):
    return render(request, 'ecom/sign_up.html')


def sign_up_submit(request):
    # print(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #form.save()
            obj = form.save(commit=False)
            obj.phone_number = "9835789000"
            obj.save()
            return render(request, 'ecom/login.html')
        else:
            return render(request, 'ecom/sign_up.html', {'form': form})
    return render(request, 'ecom/sign_up.html')
