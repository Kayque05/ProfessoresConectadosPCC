from django import forms
from django.shortcuts import render
from django.urls import reverse
from .models import Topico, Curso, Conteudo, Perguntas
from .models import Resposta
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

class Topicos(forms.ModelForm):

    class Meta:
        model = Topico
        fields = ('titulo',)

    #Verificar se há palavrão no texto
    def clean_titulo(request):
       
        titulo = request.cleaned_data['titulo']
        palavrao = ["seu macaco", "otario", "você é um troxa",
        "todos aqui são feios", "seu burro", "burro", "vacilão",
        "porno", "xvideos", "ladrão", "ladao", "burro otario preguiçoso",
        "apenas ler idiota", "plataforma lixo", "plataforma feia", "caralho",
        "cu", "buceta", "checa", "sua puta", "puta", "seu viado",
         "seu preto", "cavalo", "tição", "moleque", "prostituta", "corno", "seu corno", "sua corna",
        "seu lixo", "Desgr@ça", "desgraça",
        "sexo", "fock", "chupa meu pau", "meu pau","chupa", "sem mundial", "macaco", "incoformado", "porra",
         "seu porra", "seu otario", "capeta", "inferno",
        "gostosa", "sua gostosa", "sua linda", "sua cachorra", "cachorra", "trouxa","bicho burro da porra", "você é um trouxa",
         "besta", "gosto de sexo", "comedor de casada", "lazarento", "que povinho lazarento",
          "merda", "tomo mundo na merda", "seu moleque!", "vagabunda", "sua puta", "sua cachorra", "pornografia", "estou falando mal de alguem"]
       
        for i in titulo.split(","):
            if i in palavrao:
                return 0
            else:
                return titulo


class Respostas(forms.ModelForm):

    class Meta:
        model = Resposta
        fields = ('resposta',)
    
    def clean_resposta(request):
       
        resposta = request.cleaned_data['resposta']
        palavrao = ["trouxa","seu macaco", "otario", "você é um troxa",
        "todos aqui são feios", "seu burro", "burro", "vacilão",
        "porno", "xvideos", "ladrão", "ladao", "burro otario preguiçoso",
        "apenas ler idiota", "plataforma lixo", "plataforma feia", "caralho",
        "cu", "buceta", "checa", "sua puta", "puta", "seu viado",
         "seu preto", "cavalo", "tição", "moleque", "prostituta", "corno", "seu corno", "sua corna",
        "seu lixo", "Desgr@ça", "desgraça",
        "sexo", "fock", "chupa meu pau", "meu pau","chupa", "sem mundial", "macaco", "incoformado", "porra",
         "seu porra", "seu otario", "capeta", "inferno",
        "gostosa", "sua gostosa", "sua linda", "sua cachorra", "cachorra", "preto desgraçado",
        "filha da puta", "Filho da puta", "filho da égua", "você é um corno", "cringe", "puta que pariu",
        "merda", "seu merda", "você é um merda", "rola", "boqueteira",
         "boquetera", "mamada", "me mama", "gozei", "goza", "vou gozar", "gay",
        "vagabundo", "vagabunda", "seu vagabundo", "sua vagabunda", "pau no cu", "pnc", "estou falando mal de alguem"]
       

        
        if resposta in palavrao:
            return 0
        else:
            return resposta

class Cursos(forms.ModelForm):
    
    class Meta:

        model = Curso
        fields = ('nome_curso',)

class Conteudos(forms.ModelForm):

    class Meta:

        model = Conteudo
        fields = ('nome_conteudo','link','titulo_introducao','introducao','titulo_topico1','topico1','titulo_topico2','topico2','titulo_topico3','topico3','titulo_topico4','topico4','titulo_topico5','topico5','titulo_topico6','topico6','titulo_topico7','topico7','titulo_topico8','topico8',)


class faq(forms.ModelForm):

    class Meta:
        model = Perguntas
        fields = ('title', 'description', 'nome_curso',)