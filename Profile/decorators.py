from django.http import HttpResponse
from django.shortcuts import render,redirect


def unauthenticatedUser(viewFunction):
    # this function will not allow any user #
    def wrapperFunction(request,*args,**kwargs):
        if request.user.is_authenticated:
            # return redirect('signup')
            return HttpResponse('<h1> 404 Not Found </h1>')
        else:
            return viewFunction(request,*args,**kwargs)
    return wrapperFunction


def allowed_users(allowed_roles=[]):
    def decorator(viewFunction):
        def wrapperFunction(request, *args, **kwargs):

            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_roles:
                return viewFunction(request, *args, **kwargs)
            else:
                return HttpResponse('<h1> 404 Not Found </h1>')
        return wrapperFunction
    return decorator


def admin_only(viewFunction):
    def wrapperFunction(request, *arg, **kwargs):
        group = None
        if request.user.groups.exits():
            group = request.user.groups.all()[0].name

        if group == 'donor':
            return redirect('home')

        if group == 'admin':
            return viewFunction(request, *arg, **kwargs)

    return wrapperFunction
