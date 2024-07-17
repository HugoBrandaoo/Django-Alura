from django.shortcuts import render, get_object_or_404
from . form import FotografiaForm
from . models import Fotografia

# Responsavel por mostrar os dados retirados do banco para o template
def home(request):
    fotografia = Fotografia.objects.order_by('data').filter(publicada=True)
    return render(request,'users/home.html',{"cards":fotografia})

def imagem(request, fotografia_id):
    fotografia = get_object_or_404(Fotografia, pk=fotografia_id)
    return render(request, 'users/imagem.html', {"foto":fotografia})

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
