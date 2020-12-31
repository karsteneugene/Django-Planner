from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# @login_required decorator -> User needs to be logged in to access the page


# Register page
def register(request):
    if request.method == 'POST':

        # Fetches the form to register account
        form = UserRegisterForm(request.POST)

        # Form validation
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            # Displays a message after successfuly creating an account
            messages.success(request, 'Successfully created an account!')

            # Redirects users to the login page after creating an account
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Profile page
@login_required
def profile(request):
    if request.method == 'POST':

        # Fetches the form to update account information
        u_form = UserUpdateForm(request.POST, instance=request.user)

        # Fetches the form to change profile picture
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        # Form validation
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            # Displays a message after successfuly creating an account
            messages.success(request, 'Your account has been updated!')

            # Redirects users to the profile page after updating their account
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
