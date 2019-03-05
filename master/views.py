from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from .models import Category
from .models import Products
import hashlib
from django.http import JsonResponse
from .cat_forms import CatForm

def dashboard(request):
    return render(request, 'master/dashboard.html',{'session_user':request.session['userdata']})

def cat_list(request):
    cat = Category.objects.all()
    return render(request,'master/view_cat_list.html',{'cats':cat})

def cat_new(request):
    if request.method == 'POST':
        print(request.session['userdata'])
        # import pdb
        # pdb.set_trace()
        form = CatForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.admin_id = request.session['userdata']['user_id']
            cat.save()
            return redirect('master/cat_list')
        else:
            return render(request, 'master/add_category.html', {'form': form})
    else:
        form = CatForm()
    return render(request, 'master/add_category.html', {'form': form})

def cat_edit(request, pk):
    person = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/master/cat_list')
        else:
            return render(request, 'master/add_category.html', {'form': form})
    else:
        form = CatForm(instance=person)
    return render(request, 'master/add_category.html', {'form': form})