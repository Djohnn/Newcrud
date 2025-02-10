from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios
from django.http import HttpResponse

# Create your views here.
def create_user(request):
    if request.method == "GET":
        usuarios = Usuarios.objects.all()
        
        return render(request, 'create_user.html', {'usuarios': usuarios})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        usuarios = Usuarios(
            nome=nome,
            email=email
        )

        usuarios.save()

        return redirect('/usuarios/')
    
def delete(request, id):
    usuario = Usuarios.objects.filter(id=id)
    usuario.delete()
    return redirect('/usuarios/')

def editar(request, id):
    usuario = get_object_or_404(Usuarios, id=id)
    return render(request, 'update.html', {'usuario': usuario})


def update(request, id):
    usuario = get_object_or_404(Usuarios, id=id)
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    if not nome:
        return HttpResponse("O campo 'nome' é obrigatório", status=400)
    
    usuario.nome = nome
    usuario.email = email
    
    usuario.save()
    return redirect('/usuarios/')
    