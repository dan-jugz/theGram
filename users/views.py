from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        print("This is working bro.")
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username,"This is working")
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('/')
    else:
        #If there is no a post request just send an empty form
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})




