from django.shortcuts import render, redirect

def login_required(function):
    def wrap(request, *args, **kwargs):
        if 'userdata' not in request.session.keys():
            return redirect('/ecom/login')
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap