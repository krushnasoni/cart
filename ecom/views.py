from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from master.models import Products
from ecom.forms import SignUpForm
import hashlib
from django.http import JsonResponse
import traceback
from cartsite.decorators import login_required

def sign_up(request):
    return render(request, 'ecom/sign_up.html')


def sign_up_submit(request):
    # print(request.POST)
    try:
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
    except:
        return HttpResponse("Something went wrong.")

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
            userdata = {
                "user_id" : user.id,
                "username" : user.username,
                "user_type" : user.user_type,
            }
            request.session['userdata'] = userdata
            if user.user_type == '1':
                user_type = '1'
            else :
                user_type = '2'
            return JsonResponse({'status':'1','user_type':user_type})
        else:
            return JsonResponse({'status':'2'})
    except:
        return JsonResponse({'status':'2'})

@login_required
def welcome(request):
    return render(request, 'ecom/welcome.html',{'session_user':request.session['userdata']})

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return render(request, 'ecom/login.html')

def home(request):
    try:
        product = Products.objects.all()
        print(product)
        return render(request,'ecom/home.html', {'products':product})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def prod_details(request,pk):
    try:
        product = get_object_or_404(Products, pk=pk)
        print(product)
        return render(request, 'ecom/prod_details.html', {'products':product})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")