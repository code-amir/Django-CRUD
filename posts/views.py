from django.shortcuts import render
from login.forms import UserForm,UserProfileInfoForm
from login.models import UserProfileInfo
from datetime import *
from django.db import transaction
from django.shortcuts import render, get_object_or_404

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from .forms import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

@login_required
def home(request):
	return render(request,'posts/home.html')

@login_required
def createPost(request):
	if(request.method=="POST"):
		postForm = post()
		postForm.user = request.user
		print(request.user)
		form = PostForm(request.POST,instance = postForm)
		if form.is_valid():
			form.save()
		return render(request,'posts/home.html')
	else:
		form = PostForm()
		context = {
			'form' : form
		}
		return render(request,'posts/createPost.html',context)

@login_required
def listPost(request):
	user = request.user
	lstRequest = list(post.objects.filter())
	return render(request,"posts/listPost.html",{'lstRequest': lstRequest})
