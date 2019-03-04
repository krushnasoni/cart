from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from ecom.forms import SignUpForm
import hashlib
from django.http import JsonResponse

def sign_up(request):
    return render(request, 'ecom/sign_up.html')


def sign_up_submit(request):
    # print(request.POST)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #form.save()
            hashed_password = hashlib.sha512(request.POST['password'].encode('utf-8')).hexdigest()

            obj = form.save(commit=False)
            obj.password = hashed_password
            obj.phone_number = "9835789000"
            obj.save()
            return render(request, 'ecom/login.html')
        else:
            return render(request, 'ecom/sign_up.html', {'form': form})
    return render(request, 'ecom/sign_up.html')

def login(request):
    return render(request, 'ecom/login.html')

def login_submit(request):
    hashed_password = hashlib.sha512(request.POST['password'].encode('utf-8')).hexdigest()
    print(hashed_password)
    #return HttpResponse(request.POST['password'])
    try:
        user = Users.objects.get(email=request.POST['email'])
        print(user.password)
        if user.password == hashed_password :
            request.session['userdata'] = user.username
            return JsonResponse({'status':'1'})
        else:
            return JsonResponse({'status':'2'})
    except:
        return JsonResponse({'status':'2'})

def welcome(request):
    return render(request, 'ecom/welcome.html',{'session_data':request.session['userdata']})