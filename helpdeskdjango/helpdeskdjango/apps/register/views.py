from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    return render(request, 'register/login.html',)

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с этим адресом уже зарегистрирован')
        else:
            if form.is_valid():
                #регистрируем
                ins = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password, email=email)
                ins.email = email
                form.save_m2m()
                messages.success(request, 'Вы успешно зарегистрировались')
                return redirect('/')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register/register.html', context)