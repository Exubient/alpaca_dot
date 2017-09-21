from django.shortcuts import render

# Create your views here.
def root(request):
	return render(request, 'root/src/landing/index.html', {})

def matching(request):
	return render(request, 'root/src/blog/blog-default.html', {})

def profile(request):
	return render(request, 'root/src/blog/blog-single.html', {})

def about(request):
	return render(request, 'root/src/landing/index.html', {})

def login(request):
	return render(request, 'root/src/account/contact.html', {})

def signUp(request):
	return render(request, 'root/src/account/signUp.html', {})

