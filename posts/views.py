from django.shortcuts import render,redirect
from login.forms import UserForm,UserProfileInfoForm
from login.models import UserProfileInfo
from datetime import *
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from . import models

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import *
from django.views import generic
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

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
	lstRequest = list(post.objects.filter(user=user))
	return render(request,"posts/listPost.html",{'lstRequest': lstRequest})

@login_required
def post_detail_view(request,pk):
	post_dt=post.objects.get(pk=pk)
	# print(post_dt)
	return render(request,"posts/posts_detail.html",{"post_dt":post_dt})


def post_update(request,pk):
	template="posts/createPost.html"
	post_dt=get_object_or_404(post,pk=pk)
	form = PostForm(request.POST or None,  instance=post_dt)
	if form.is_valid():
		form.save()
		return redirect('posts:listPost')
	context = {
		'form' : form
	}

	# print(post_dt)
	return render(request,template,context)


def post_delete(request,pk):
	template="posts/post_delete.html"
	post_dt=get_object_or_404(post,pk=pk)
	if (request.method=="POST"):
		post_dt.delete()
		return redirect('posts:listPost')
	context = {
		'post_dt' : post_dt
	}
	return render(request,template,context)
