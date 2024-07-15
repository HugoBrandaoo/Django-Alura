from django.urls import path
from . views import home, imagem,FotoFR, teste

urlpatterns = [
    path('', home, name='home'),
    path('imagem/', imagem, name='imagem'),
    path('novo/', FotoFR),
    path('teste/', teste)
]
