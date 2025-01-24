from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        # Autenticar o usuário
        user = authenticate(request, username=usuario, password=senha)
        
        if user is not None:
            # Se o usuário foi autenticado corretamente, fazer login
            auth_login(request, user)
            return redirect('index')
        else:
           context = {'mensagem':'Usuário ou senha inválidos.'}

        return render(request, 'login.html', context)
    
    context = {}

    return render(request, 'login.html', context)