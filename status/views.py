from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from status.models import Status
from django.shortcuts import render, get_object_or_404
from .texts import IMC

# Create your views here.

# Login

def login_user(request):
    return render(request, 'login_user.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

def submit_logout(request):
    logout(request)
    return redirect('/')

def cadastro(request):
    return render(request, 'cadastro.html')
def submit_cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password)
            status = Status(usuario=user, nome='default', peso=0, altura=0)
            status.save()
            return redirect('/')
        else:
            error_message = "As senhas não correspondem."
            return redirect('/')

    return redirect('/')

# Main
    
@login_required(login_url='/login/')
def main(request):
    usuario = request.user
    status = Status.objects.get(usuario=usuario)
    
    lista = IMC(status.peso, status.altura)
    
    estatistica = lista[0]
    descricao = lista[1]
    
    dados = {'status' : status, 'estatistica' : estatistica, 'descricao' : descricao}
    
    
    
    return render(request, 'main.html', dados)

    

# Update

@login_required(login_url='/login/')
def update_status(request, id):
    usuario = request.user
    status = Status.objects.get(usuario=usuario)
    dados = {'status' : status}
    return render(request, 'update_status.html', dados)

@login_required(login_url='/login/')
def submit_update_status(request, id):
    if request.method == 'POST':
        usuario = request.user
        status = Status.objects.get(usuario=usuario)
        nome = request.POST.get('nome')  # Substitua 'nome' pelo nome do campo no seu template
        peso = request.POST.get('peso')  # Substitua 'peso' pelo nome do campo no seu template
        altura = request.POST.get('altura')  # Substitua 'altura' pelo nome do campo no seu template
        # Atualize os dados do status com base nos dados do formulário
        status.nome = nome
        status.peso = peso
        status.altura = altura
        status.save()
        return redirect('/')  # Redirecione para a página principal ou para a página desejada após a atualização
    else:
        return redirect('/')  # Redirecione para a página principal ou para a página desejada em caso de requisição não-POST