from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from .models import Category
from .models import Products
import hashlib
from django.http import JsonResponse
from .cat_forms import CatForm
from .prod_forms import ProdForm
import traceback
from .prod_forms import ImageFileUploadForm
from django.core.files.storage import FileSystemStorage
from cartsite.decorators import login_required

def dashboard(request):
    return render(request, 'master/dashboard.html',{'session_user':request.session['userdata']})

def cat_list(request):
    try:
        cat = Category.objects.all()
        return render(request, 'master/view_cat_list.html', {'cats': cat})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

@login_required
def cat_new(request):
    try:
        if request.method == 'POST':
            print(request.session['userdata'])
            # import pdb
            # pdb.set_trace()
            form = CatForm(request.POST)
            if form.is_valid():
                cat = form.save(commit=False)
                cat.admin_id = request.session['userdata']['user_id']
                cat.save()
                return redirect('/master/cat_list')
            else:
                return render(request, 'master/add_category.html', {'form': form})
        else:
            form = CatForm()
        return render(request, 'master/add_category.html', {'form': form})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def cat_edit(request, pk):
    try:
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
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def cat_del(request, pk):
    try:
        Category.objects.get(pk=pk).delete()
        return redirect('/master/cat_list')
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

#PRODUCT CRUD

def prod_list(request):
    try:
        prod = Products.objects.all()
        return render(request,'master/view_prod_list.html',{'prods':prod})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def prod_new(request):
    try:
        if request.method == 'POST':
            print(request.session['userdata'])
            # import pdb
            # pdb.set_trace()
            form = ProdForm(request.POST)
            if form.is_valid():
                prod = form.save(commit=False)
                prod.admin_id = request.session['userdata']['user_id']
                prod.save()
                return redirect('/master/prod_list')
            else:
                return render(request, 'master/add_product.html', {'form': form})
        else:
            form = ProdForm()
        return render(request, 'master/add_product.html', {'form': form})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def prod_edit(request, pk):
    try:
        person = get_object_or_404(Products, pk=pk)
        if request.method == 'POST':
            form = ProdForm(request.POST, instance=person)
            if form.is_valid():
                form.save()
                return redirect('/master/prod_list')
            else:
                return render(request, 'master/add_product.html', {'form': form})
        else:
            form = ProdForm(instance=person)
        return render(request, 'master/add_product.html', {'form': form})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def prod_del(request, pk):
    try:
        Products.objects.get(pk=pk).delete()
        return redirect('/master/prod_list')
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def gallary(request, pk):
    try:
        product = get_object_or_404(Products, pk=pk)
        print(product.image)
        import ast
        new_list = ast.literal_eval(product.image)
        return render(request, 'master/gallary.html', {'id':pk ,'product':product,'image_list':new_list})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def gallary_upload(request):
    try:
        pk = request.POST['prod_id']
        product = get_object_or_404(Products, pk=pk)
        if request.method == 'POST':
            print(request.FILES)
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)

            print(product.image)
            if product.image == '' or product.image == None:
                uploaded_file_url = [fs.url(filename)]
            else :
                import ast
                new_list = ast.literal_eval(product.image)
                new_list.append(fs.url(filename))
                uploaded_file_url = new_list
                print(uploaded_file_url)

            count = Products.objects.filter(id=pk).update(image=uploaded_file_url)
            if count >= 1 :
                return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
            else:
                return JsonResponse({'error': True, 'message': 'Uploaded unsuccessful'})
        else:
            form = ImageFileUploadForm()
            return render(request, 'master/gallary.html', {'form': form})
    except Exception as e:
        traceback.print_exc()
        return HttpResponse("Something went wrong.")

def delete_image(request) :
    pk = request.POST['id']
    img = request.POST['img']
    product = Products.objects.get(id=pk)
    import ast
    new_list = ast.literal_eval(product.image)
    new_list.remove(img)
    count = Products.objects.filter(id=pk).update(image=new_list)
    if count >= 1:
        return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
    else:
        return JsonResponse({'error': True, 'message': 'Uploaded unsuccessful'})
