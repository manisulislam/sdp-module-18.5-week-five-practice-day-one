from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
# Create your views here.
def register(request):
    if request.method=='POST':
        register_form=RegistrationForm(request.POST)
        if register_form.is_valid():
           
            register_form.save()
            return redirect("signIn")
            
    else:
        register_form=RegistrationForm()
        
    return render(request, "register.html",{"form":register_form, "type":"Register"})



# sign in 

def signIn(request):
    if request.method=='POST':
        signIn_form= AuthenticationForm(request=request, data=request.POST)
        if signIn_form.is_valid():
            user_name=signIn_form.cleaned_data["username"]
            user_pass=signIn_form.cleaned_data["password"]
            user=authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request,user)
                messages.success(request, "Logged In Successfully")
                return redirect("profile")
            else:
                messages.info(request, "Enter valid user and password")
    else:
        signIn_form= AuthenticationForm()
    return render(request, "register.html", {"form":signIn_form, "type":"Sign In"})

# profile page

@login_required
def profile(request):
    return render(request, "profile.html")


# sign out
def signOut(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("home")

@login_required
def pass_change_with_old(request):
    if request.method=='POST':
        change_pass_form=PasswordChangeForm(request.user, request.POST)
        if change_pass_form.is_valid():
            user=change_pass_form.save()
            update_session_auth_hash(request,user)
            return redirect("signIn")
            
    else:
       change_pass_form=PasswordChangeForm(request.user)
        
    return render(request, "register.html",{"form":change_pass_form, "type":"Change your password with old password"})


@login_required
def pass_change_without_old(request):
    if request.method=='POST':
        change_pass_form=SetPasswordForm(request.user, request.POST)
        if change_pass_form.is_valid():
            user=change_pass_form.save()
            update_session_auth_hash(request,user)
            return redirect("signIn")
            
    else:
       change_pass_form=SetPasswordForm(request.user)
        
    return render(request, "register.html",{"form":change_pass_form, "type":"Change your password with out old password"})
