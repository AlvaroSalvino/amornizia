from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)

def presentes(request):
    context = {}
    return render(request, 'presentes.html', context)

def carta(request):
    context = {}
    return render(request, 'carta.html', context)

def meu_coracao(request):
    context = {}
    return render(request, 'meu_coracao.html', context)

def snape(request):
    context = {}
    return render(request, 'snape.html', context)
