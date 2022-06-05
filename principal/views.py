from msilib.schema import Class
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Curso, Perguntas, Conteudo, Topico, Resposta, Material


from .forms import Topicos, Respostas

from django.contrib import messages
from django.core.paginator import Paginator


##################### Sistema do FAQ ##############################

# - Pagina Home - #

def telahome(request):
    cursos_m = Curso.objects.all()

    context = {

        'n_curso': cursos_m,
    }  
    return render(request, 'principals/telahome.html', context)

def listarConteudo(request, conteudo_id):

    viewConteudo = get_object_or_404(Curso, pk=conteudo_id)
    conteudo = Resposta.objects.all()

    context ={
        'curso': viewConteudo,
        'conteudo': conteudo,
    }
    return render(request, 'principals/curso.html', context)

#Listar Material
def listarMaterial(request, id):
    conteudo = Conteudo.objects.get(pk=id)
    material = Material.objects.all()

    context ={
        'conteudo': conteudo,
        'material':material,
    }
    return render(request, 'principals/listarMaterial.html', context)
########################################## F A Q ###############################################
def Pergunta(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        perguntas = Perguntas.objects.filter(title__icontains=search)
    elif filter:
        perguntas = Perguntas.objects.filter(nome_curso = filter)
    else:
        perguntas_list = Perguntas.objects.all()
        paginator = Paginator(perguntas_list, 5)
        page = request.GET.get('page')
        perguntas = paginator.get_page(page)
    return render(request, 'principals/perguntas.html', {'perguntas': perguntas})

def detailPerguntas(request, id):
    detalhePergunta = get_object_or_404(Perguntas, pk=id)
    return render(request, 'principals/DetalhePerguntas.html', {'detalheP': detalhePergunta})

#def detailPerguntas(request, perguntas_id):

 #   try:
        #detailPerguntas = CursoFaq.objects.get(id= perguntas_id)
    #except CursoFaq.DoesNotExist:
        ##detailPerguntas = None
    
    #context = {
        #'detailPerguntas':detailPerguntas,
    #}
    #return render(request, 'principals/perguntas.html', context)





#def acessarCurso(request, id):
   # curso = Curso.objects.get(pk=id)
   # cursoFaq = CursoFaq.objects.get(curso = curso)
    #perguntas = Perguntas.objects.get(curso_faq = cursoFaq)
   # conteudo = Conteudo.objects.get(curso = curso)
    #context ={
       # "curso" : curso,
        #"cursoFaq": cursoFaq,
       # "conteudo" : conteudo,
        #"perguntas" : perguntas
    #}

    return render(request, 'principals/paginacurso.html', context)

#def detailPerguntas(request, id_faq):
   # cursoFaq = CursoFaq.objects.get(pk = id_faq)
    #perguntas = Perguntas.objects.get(curso_faq = cursoFaq)

    #context = {
        #'perguntas': perguntas,
    #}
   # return render(request, 'principals/perguntas.html', context)


#def detailPerguntas(request, id):
    #cursoFaq = CursoFaq.objects.get(pk = id)
   # perguntas = Perguntas.objects.get(curso_faq = cursoFaq)

    #context = {
        #'perguntas': perguntas,
    #}
   # return render(request, 'principals/perguntas.html', context)

#def detailPerguntas(request, id):
    #cursoFaq = CursoFaq.objects.get(pk = id)
   # perguntas = Perguntas.objects.get(curso_faq = cursoFaq)

   # context = {
        #'perguntas': perguntas,
  #  }
    #return render(request, 'principals/perguntas.html', context)


############################### - Topico - ###########################################

def PaginaTopicos(request):
    search = request.GET.get('search')
    Topico.objects.filter(titulo__icontains ="0").delete()
    if search:
       
        comenta = Topico.objects.filter(titulo__icontains=search)
 
    else:
 
        comenta_list = Topico.objects.all()
        paginator = Paginator(comenta_list, 3)
 
        page = request.GET.get('page')
 
        comenta = paginator.get_page(page)
 
    return render(request, 'principals/topicos.html', {'comenta': comenta})

def viewTopico(request, id_topico):
    viewTopico = get_object_or_404(Topico, pk=id_topico)
    Resposta.objects.filter(resposta__icontains ="0").delete()
    resposta = Resposta.objects.all()

    context ={
        'topico': viewTopico,
        'resposta': resposta,
    }
    return render(request, 'principals/viewRespostas.html', context)
 
def novoTopico(request):
    if request.method == 'POST':
        form = Topicos(request.POST)
 
        if form.is_valid():
            coment = form.save(commit=False)
            coment.user = request.user
            coment.save()
            return redirect('/Topico/')
            
    else:
        form = Topicos()
        return render(request, 'principals/addTopico.html', {'form': form})

#-#-#-#-#-#-#-#-#- Meus Tópicos #-#-#-#-#-#-#-#-

#Listar Topicos do usuário logado
def meusTopicos(request):
    search = request.GET.get('search')
    Topico.objects.filter(titulo__icontains ="0").delete()
    if search:
       
        topico = Topico.objects.filter(titulo__icontains=search, user=request.user)
 
    else:
 
        topico_list = Topico.objects.all().filter(user=request.user)
        paginator = Paginator(topico_list, 10)
 
        page = request.GET.get('page')
 
        topico = paginator.get_page(page)
 
    return render(request, 'principals/meusTopicos.html', {'topico': topico})

#Editar Tópico
def editTopico(request, id_topico):
    topico = get_object_or_404(Topico, pk=id_topico)
    form = Topicos(instance=topico)
 
    if(request.method == 'POST'):
        form = Topicos(request.POST, instance = topico)
 
        if(form.is_valid()):
            topico.save()
            return redirect('/Topico/view-topicos/')
        else:
            return render(request, 'principals/edit-Topico.html', {'form':form, 'topico':topico})
 
    else:
        return render(request, 'principals/edit-Topico.html', {'form':form, 'topico':topico})

#Deletar Topico
def deletarTopico(request, id_topico):
    topico = get_object_or_404(Topico, pk=id_topico)
    topico.delete()
 
    messages.info(request, 'Tópico Deletado com sucesso.')
    return redirect('/Topico/view-topicos/')








def deletarComentario(request, id):
    comenta = get_object_or_404(Topico, pk=id)
    comenta.delete()
 
    messages.info(request, 'Tarefa Deletada com sucesso.')
    return redirect('/comenta/')




######################## Responder Comentário #########################################################


#view que add um comentário ao tópico
def addResposta(request, id):

    topico = Topico.objects.get(id=id)
    if request.method == 'POST':
        form = Respostas(request.POST)

        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.topico = topico
            resposta.user = request.user
            resposta.save()
            return redirect('/Topico/')
    else: 
        form = Respostas()
        return render(request, 'principals/add_Resposta.html', {'form': form, 'topico':topico})

def minhasRespostas(request):
    Resposta.objects.filter(resposta__icontains ="0").delete()
    resposta_list = Resposta.objects.filter(user=request.user)
    paginator = Paginator(resposta_list, 3)
 
    page = request.GET.get('page')
 
    resposta = paginator.get_page(page)
 
    return render(request, 'principals/minhasRespostas.html', {'resposta': resposta})

def editResposta(request, id_resposta):
    resposta = get_object_or_404(Resposta, pk=id_resposta)
    form = Respostas(instance=resposta)
 
    if(request.method == 'POST'):
        form = Respostas(request.POST, instance = resposta)
 
        if(form.is_valid()):
            resposta.save()
            return redirect('/Topico/view-respostas/')
        else:
            return render(request, 'principals/edit-Topico.html', {'form':form, 'resposta':resposta})
 
    else:
        return render(request, 'principals/edit-Topico.html', {'form':form, 'resposta':resposta})

def deletarResposta(request, id_resposta):
    topico = get_object_or_404(Resposta, pk=id_resposta)
    topico.delete()
 
    messages.info(request, 'Tópico Deletado com sucesso.')
    return redirect('/Topico/view-respostas/')