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

    def __str__(self):
        return self.nome_conteudo

class Material(models.Model):
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)
    titulo_introducao = models.CharField(max_length=255)
    introducao = models.CharField(max_length=255)
    primeiro_passo_titulo = models.CharField(max_length=255)
    primeiro_passo = models.TextField()
    segundo_passo = models.TextField()
    terceira_passo = models.TextField()
    quarto_passo = models.TextField()
    quinto_passo = models.TextField()
    sexto_passo = models.TextField()
    setimo_passo = models.TextField()
    oitavo_passo = models.TextField()
    nono_passo = models.TextField()
    decimo_passo = models.TextField()
    onze_passo = models.TextField()
    doze_passo = models.TextField()
    def __str__(self):
        return self.titulo_introducao
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