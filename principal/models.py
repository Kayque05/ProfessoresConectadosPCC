from django.db import models
from django.contrib.auth import get_user_model

class Curso(models.Model):
    nome_curso = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_curso

class Perguntas(models.Model):
    
    CURSO = (
        ('Google','Google'),
        ('Microsoft','Microsoft'),
        ('Web', 'Web'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    nome_curso = models.CharField(
        max_length=10,
        choices= CURSO,

    )
    def __str__(self):
        return self.title

class Conteudo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome_conteudo = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    titulo_introducao = models.CharField(max_length=255)
    introducao = models.TextField()
    titulo_topico1 = models.CharField(max_length=255)
    topico1 = models.TextField()
    titulo_topico2 = models.CharField(max_length=255)
    topico2 = models.TextField()
    titulo_topico3 = models.CharField(max_length=255)
    topico3 = models.TextField()
    titulo_topico4 = models.CharField(max_length=255)
    topico4 = models.TextField()
    titulo_topico5 = models.CharField(max_length=255)
    topico5 = models.TextField()
    titulo_topico6 = models.CharField(max_length=255)
    topico6 = models.TextField()
    titulo_topico7 = models.CharField(max_length=255)
    topico7 = models.TextField()
    titulo_topico8 = models.CharField(max_length=255)
    topico8 = models.TextField()
    def __str__(self):
        return self.nome_conteudo

class Topico(models.Model):
   
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    def __str__(self):
        return self.titulo
 
class Resposta(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    resposta = models.CharField(max_length=255)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    def __str__(self):
        return self.resposta