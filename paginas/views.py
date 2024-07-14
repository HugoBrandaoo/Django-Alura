from django.shortcuts import render
from . form import FotografiaForm
from .models import Fotografia
# Create your views here.
def home(request):
    fotografia = Fotografia.objects.all()
    return render(request,'users/home.html',{"card":fotografia})

def imagem(request):
    return render(request, 'users/imagem.html')

def FotoFR(request):
    form = FotografiaForm(request.POST or None)

    # if form.is_valid:
    #     form.save()
    #     return home(request)

    return render(request,'users/form.html',{"form":form})