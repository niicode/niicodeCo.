from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/users/login/')
        else:
            return render(request, 'signup.html', {'signup_form': form})
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'signup_form': form})


def login_view(request):
    # if request.user.is_authenticated():
    #     redirect('/gideon/')
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            userobject = authenticate(phone_number=phone_number, password=password)

            if userobject is not None and userobject.is_active:
                login(request, userobject)
                return redirect('/gideon/')
            else:
                return render(request, 'login.html', {'login_form': form})
        else:
            return render(request, 'login.html', {'login_form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'login_form': form})


