from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # form.comment = 'bhains ki taang'
            # form._age = 20
            # form._Intro = 'Abbay oye'
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account has now been created! You are now able to login!')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {
            "form": form
        })

         
    else:    
        form = UserRegisterForm()
        return render(request, 'users/register.html', {
            "form": form
        })

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        print(f"U FORM: {u_form}")
        

        p_form = ProfileUpdateForm(request.POST, request.FILES, 
        instance = request.user.profile)
        print(f"P FORM: {p_form}")

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # This is how to add a success message into the Request Context
            messages.success(request, f'Your profile has now been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        "u_form":u_form,
        "p_form":p_form
    }
    return render(request, "users/profile.html", context)