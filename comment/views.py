from django.shortcuts import render
from django.contrib import messages
from .models import post,post_M
from .forms import commentform,post_f
# Create your views here.
def comment(request):
    if request.method == 'POST':
        frm = commentform(request.POST)
        if frm.is_valid():
            title = frm.cleaned_data['title']
            body = frm.cleaned_data['body']
            buy = post(title=title, body=body)
            buy.save()
            messages.success(request, 'Your massage has Submit')

    return render(request,'comment.html',{'form':frm})

def post(request):
    if request.method == 'POST':
        frm = post_f(request.POST)
        if frm.is_valid():
            title = frm.cleaned_data['title']
            email = frm.cleaned_data['email']
            buy = post_M(title=title, email=email)
            buy.save()
            messages.success(request, 'Your form has submit')
    return render(request, 'post.html',{'form':frm})