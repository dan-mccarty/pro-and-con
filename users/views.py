from django.shortcuts import render

# Create your views here.


def login(request):
    """ login """

    template = '/users/login.html'
    context = {}
    return render(request, template, context)


def logout(request):
    """ logout """

    template = '/users/logout.html'
    context = {}
    return render(request, template, context)


def sign_up(request):
    """ sign_up """

    template = '/users/sign_up.html'
    context = {}
    return render(request, template, context)


def password_change(request):
    """ password_change """

    template = '/users/password_change.html'
    context = {}
    return render(request, template, context)


def password_confirm(request):
    """ password_confirm """

    template = '/users/password_confirm.html'
    context = {}
    return render(request, template, context)


def password_forgot(request):
    """ password_forgot """

    template = '/users/password_forgot.html'
    context = {}
    return render(request, template, context)


def password_reset(request):
    """ password_reset """

    template = '/users/password_reset.html'
    context = {}
    return render(request, template, context)
    
    