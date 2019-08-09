from django.shortcuts import render

def mostar_home (request):
	return render (request, 'home.html')

def mostar_cadastro (request):
	return render (request, 'cadastro.html')

def mostrar_usuario (request):
	return render (request, 'usuario.html')

def mostrar_informacoes (request):
	return render (request, 'informacoes.html')

	


















# Create your views here.
