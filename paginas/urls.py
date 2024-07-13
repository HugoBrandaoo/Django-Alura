from django.urls import path
from . views import home, imagem

urlpatterns = [
    path('', home, name='home'),
    path('imagem/', imagem, name='imagem')
]
