from multiprocessing import context
from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

def main	(request):
	context = {'home':'/home'}
	return render(request, 'store/main.html', context)

def login	(request):
	context = {'login':'/login'}
	return render(request, 'store/login.html', context)
