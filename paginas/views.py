from django.shortcuts import render, redirect
from . form import FotografiaForm
from . models import Fotografia

# Responsavel por mostrar os dados retirados do banco para o template
def home(request):
    fotografia = Fotografia.objects.all()
    return render(request,'users/home.html',{"cards":fotografia})

def imagem(request):
    return render(request, 'users/imagem.html')

# Viwer responsavel por criar um formulario
def FotoFR(request):
    form = FotografiaForm(request.POST or None)
    try:
        if form.is_valid:
            form.save(request)
            return home(request)
    except Exception as e:
        print(e)
    
    return render(request,'users/form.html',{"form":form})


def teste(request):
    fotografia = Fotografia.objects.all()
    return render(request, 'users/teste.html',{"cards":fotografia})