from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.core.mail import message
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import request
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,get_user_model
from .regi import register_f,change_u,UserProfileForm
from .models import form_model,UserProfile
from .forms import formf
from django.views.generic import ListView, DetailView

# Gmail Verification Import ----------------------------
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
UserModel=get_user_model()
# Create your views here.
# Login --------------------------------------------
def log(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data=request.POST)
        if frm.is_valid():
            usern = frm.cleaned_data['username']
            passw = frm.cleaned_data['password']
            user = authenticate(username=usern, password=passw)
            if user is not None:
                login(request,user)
                messages.success(request, 'Your Login Was Successfully')
                return HttpResponseRedirect('/loginformf')
            else:
                messages.warning(request,'Invalid Your Username Or Password')
        else:
                messages.warning(request,'Invalid Your Username Or Password')
    
    else:
        frm = AuthenticationForm()
                
    return render(request,'log.html',{'form':frm})

# Register + Email Verification ---------------------------------------------------
def register(request):
    if request.method == 'POST':
        frm = register_f(request.POST)
        if frm.is_valid():
            user=frm.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'
            message = render_to_string('account.html', {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            send_mail = frm.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message, to=[send_mail])
            email.send()
            messages.info(request, 'Activate your account from the mail you provided')
            return HttpResponseRedirect('/Register_Mail')

    else:
        frm = register_f()
    return render(request,'regi.html',{'form':frm})

def activate(request, uidb64, token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=UserModel._default_manager.get(pk=uid)
    except(TypeError,ValueError, OverflowError, User.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        messages.success(request, "Your account is activated now, you can now log in")
        return HttpResponseRedirect('/loginf')
    else:
        messages.warning(request, "activate link is invalid")
        return HttpResponseRedirect('/online')



# Register redirect ------------------------------------
def register_redirect(request):
    return render(request, 'register_mail.html')



# Form ----------------------------------------------
def form(request):
    if request.method == 'POST':
        frm = formf(request.POST)
        if frm.is_valid():
            username = frm.cleaned_data['username']
            email = frm.cleaned_data['email']
            phone = frm.cleaned_data['phone']
            rollnumber = frm.cleaned_data['rollnumber']
            regnumber = frm.cleaned_data['regnumber']
            Choise = frm.cleaned_data['Choise']
            data = form_model(username=username,email=email,phone=phone,rollnumber=rollnumber,regnumber=regnumber,Choise=Choise)
            data.save()
            messages.success(request, 'Your Form Submited Successfully')
            return HttpResponseRedirect('/Redirect_Form')
    
    else:
        frm = form_model()
            
    return render(request,'index.html',{'form':frm})


def redirect_f(request):
    return render(request,'redi.html')


# Change user ---------------------------------------------
def change_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm = change_u(request.POST, instance = request.user)
            if frm.is_valid():
                frm.save()
                messages.success(request, 'You are Successfully Change User')
                return HttpResponseRedirect('/register__F')
        else:
            frm = change_u(instance = request.user)
        return render(request,'change_u.html',{'form':frm})
    
    else:
        return HttpResponseRedirect('/change_u')

# Profile -----------------------------------------------------
def userprofile(request):
    try:
        instance=UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        instance=None
    if request.method == 'POST':
        if instance:
            form=UserProfileForm(request.POST,request.FILES, instance=instance)
        else:
            form=UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request, "Successfully Saved Your Profile")
            return redirect('loginformf')
    else:
        form=UserProfileForm(instance=instance)
    context={
        'form':form

    }
    return render(request, 'userprofile.html',context)
            
            
def home_P(request):
    return render(request, 'home.html')
            

