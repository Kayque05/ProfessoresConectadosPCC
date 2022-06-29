from msilib.schema import Class
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse
from .models import Curso, Perguntas, Conteudo, Topico, Resposta


from .forms import Topicos, Respostas, Cursos, Conteudos, faq

from django.contrib import messages
from django.core.paginator import Paginator


##################### Sistema do FAQ ##############################

# - Pagina Home - #

################################# - Visualizar Cursos - #########################
@login_required
def telahome(request):
    cursos_m = Curso.objects.all()

    context = {

        'n_curso': cursos_m,
    }  
    return render(request, 'principals/telahome.html', context)


###### - Adicionar Curso -- #######
def addCurso(request):

    if request.method == 'POST':
        form = Cursos(request.POST)
 
        if form.is_valid():
            curso = form.save(commit=False)
            curso.save()
            return redirect('/')
            
    else:
        form = Cursos()
        return render(request, 'admin/add_curso.html', {'form': form})
        

############# - Deletar Curso - ############
@login_required
def deletarCurso(request, id_curso):
    curso = get_object_or_404(Curso, pk=id_curso)
    curso.delete()
    messages.info(request, 'Tópico Deletado com sucesso.')
    return redirect('/')


########### - Editar Curso - ############
@login_required
def editCurso(request, id_curso):
    curso = get_object_or_404(Curso, pk=id_curso)
    form = Cursos(instance=curso)
 
    if(request.method == 'POST'):
        form = Cursos(request.POST, instance = curso)
 
        if(form.is_valid()):
            curso.save()
            return redirect('/')
        else:
            return render(request, 'admin/edit_curso.html', {'form':form, 'topico':curso})
 
    else:
        return render(request, 'admin/edit_curso.html', {'form':form, 'topico':curso})

############################################### - Conteudo - #########################################

########## - Listar Conteúdo - ############
@login_required
def listarConteudo(request, conteudo_id):

    viewConteudo = get_object_or_404(Curso, pk=conteudo_id)
    conteudo = Resposta.objects.all()

    context ={
        'curso': viewConteudo,
        'conteudo': conteudo,
    }
    return render(request, 'principals/curso.html', context)

########## - Adicionar Conteudo - ############
@login_required
def addConteudo(request, id_conteudo):

    curso = Curso.objects.get(id=id_conteudo)
    if request.method == 'POST':
        form = Conteudos(request.POST)

        if form.is_valid():
            conteudo = form.save(commit=False)
            conteudo.curso = curso
            conteudo.save()
            return redirect('/')
    else: 
        form = Conteudos()
        return render(request, 'admin/add_conteudo.html', {'form': form})

########## - Deletar Conteudo - ##############
def deletarConteudo(request, id_conteudo):
    conteudo = get_object_or_404(Conteudo, pk=id_conteudo)
    conteudo.delete()
    messages.info(request, 'Tópico Deletado com sucesso.')
    return redirect('/')

################## - Editar Conteudo - ###############

@login_required
def editConteudo(request, id_conteudo):
    conteudo = get_object_or_404(Conteudo, pk=id_conteudo)
    form = Conteudos(instance=conteudo)
 
    if(request.method == 'POST'):
        form = Conteudos(request.POST, instance = conteudo)
 
        if(form.is_valid()):
            conteudo.save()
            return redirect('/')
        else:
            return render(request, 'principals/edit-Topico.html', {'form':form })
 
    else:
        return render(request, 'principals/edit-Topico.html', {'form':form})

########################### Visualizar Conteudo ##################################
@login_required
def VisualizarConteudo(request, id):
    
    conteudo = Conteudo.objects.get(pk=id)

    context ={
        'conteudo': conteudo,
        
    }
    return render(request, 'principals/listarConteudo.html', context)

########################################## F A Q ###############################################

############ Listar Pergunta ##############
@login_required
def Pergunta(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        perguntas = Perguntas.objects.filter(title__icontains=search)
    elif filter:
        perguntas = Perguntas.objects.filter(nome_curso = filter)
    else:
        perguntas = Perguntas.objects.all()
        
    return render(request, 'principals/perguntas.html', {'perguntas': perguntas})

############## Detalhar Pergunta #############
@login_required
def detailPerguntas(request, id):
    detalhePergunta = get_object_or_404(Perguntas, pk=id)
    return render(request, 'principals/DetalhePerguntas.html', {'detalheP': detalhePergunta})

# Adicionar pergunta frequente
@login_required
def addPerguntaFrequente(request):
    if request.method == 'POST':
        form = faq(request.POST)
 
        if form.is_valid():
            pergunta = form.save(commit=False)
            pergunta.save()
            return redirect('/perguntas/')
            
    else:
        form = faq()
        return render(request, 'admin/admin_faq.html', {'form': form})

# Edit FAQ

def editPerguntasFrequentes(request, id_pergunta):
    pergunta = get_object_or_404(Perguntas, pk=id_pergunta)
    form = faq(instance=pergunta)
 
    if(request.method == 'POST'):
        form = faq(request.POST, instance = pergunta)
 
        if(form.is_valid()):
            pergunta.save()
            return redirect('/perguntas/')
        else:
            return render(request, 'admin/admin_faq.html', {'form':form})
 
    else:
        return render(request, 'admin/admin_faq.html', {'form':form})

# Deletar FAQ 

@login_required
def deletarPergunta(request, id_pergunta):
    pergunta = get_object_or_404(Perguntas, pk=id_pergunta)
    pergunta.delete()
 
    messages.info(request, 'Tópico Deletado com sucesso.')
    return redirect('/perguntas/')

############################### - Topico - ###########################################


############## Listar Tópicos ################
@login_required
def PaginaTopicos(request):
    search = request.GET.get('search')
    Topico.objects.filter(titulo__icontains ="0").delete()
    if search:
       
       topico = Topico.objects.filter(titulo__icontains=search)
 
    else:
 
        topico = Topico.objects.all()
        
 
    return render(request, 'principals/topicos.html', {'comenta': topico})

################# Visualizar Tópicos ####################
@login_required
def viewTopico(request, id_topico):
    viewTopico = get_object_or_404(Topico, pk=id_topico)
    Resposta.objects.filter(resposta__icontains ="0").delete()
    resposta = Resposta.objects.all()

    context ={
        'topico': viewTopico,
        'resposta': resposta,
    }
    return render(request, 'principals/viewRespostas.html', context)


##################### Criar tópico ###################
@login_required
def novoTopico(request):
    if request.method == 'POST':
        form = Topicos(request.POST)
 
        if form.is_valid():
            coment = form.save(commit=False)
            coment.user = request.user
            coment.save()
            return redirect('/topico/')
            
    else:
        form = Topicos()
        return render(request, 'principals/addTopico.html', {'form': form})

#-#-#-#-#-#-#-#-#- Meus Tópicos #-#-#-#-#-#-#-#-

#Listar Topicos do usuário logado
@login_required
def meusTopicos(request):
    search = request.GET.get('search')
    Topico.objects.filter(titulo__icontains ="0").delete()
    if search:
       
        topico = Topico.objects.filter(titulo__icontains=search, user=request.user)
 
    else:
 
        topico = Topico.objects.all().filter(user=request.user)
       
 
    return render(request, 'principals/meusTopicos.html', {'topico': topico})

#Editar Tópico do usuário logado
@login_required
def editTopico(request, id_topico):
    topico = get_object_or_404(Topico, pk=id_topico)
    form = Topicos(instance=topico)
 
    if(request.method == 'POST'):
        form = Topicos(request.POST, instance = topico)
 
        if(form.is_valid()):
            topico.save()
            return redirect('/topico/view-topicos/')
        else:
            return render(request, 'principals/edit-Topico.html', {'form':form, 'topico':topico})
 
    else:
        return render(request, 'principals/edit-Topico.html', {'form':form, 'topico':topico})

#Deletar Topico do usuário logado
@login_required
def deletarTopico(request, id_topico):
    topico = get_object_or_404(Topico, pk=id_topico)
    topico.delete()
 
    messages.info(request, 'Tópico Deletado com sucesso.')
    return redirect('/topico/view-topicos/')




######################## Comentário #####################################


#view que add um comentário ao tópico
@login_required
def addResposta(request, id):

    topico = Topico.objects.get(id=id)
    if request.method == 'POST':
        form = Respostas(request.POST)

        if form.is_valid():
            resposta = form.save(commit=False)
            resposta.topico = topico
            resposta.user = request.user
            resposta.save()
            return redirect('/topico/')
    else: 
        form = Respostas()
        return render(request, 'principals/add_Resposta.html', {'form': form, 'topico':topico})

# Respostas Usuário Logado
@login_required
def minhasRespostas(request):
    Resposta.objects.filter(resposta__icontains ="0").delete()
    resposta_list = Resposta.objects.filter(user=request.user)
    
    resposta = resposta_list
 
    return render(request, 'principals/minhasRespostas.html', {'resposta': resposta})

# Edição de respostas do usuário logado
@login_required
def editResposta(request, id_resposta):
    resposta = get_object_or_404(Resposta, pk=id_resposta)
    form = Respostas(instance=resposta)
 
    if(request.method == 'POST'):
        form = Respostas(request.POST, instance = resposta)
 
        if(form.is_valid()):
            resposta.save()
            return redirect('/topico/view-respostas/')
        else:
            return render(request, 'principals/edit-Topico.html', {'form':form, 'resposta':resposta})
 
    else:
        return render(request, 'principals/edit-Topico.html', {'form':form, 'resposta':resposta})

# Exclusão de Resposta do usuário logado
@login_required
def deletarResposta(request, id_resposta):
    topico = get_object_or_404(Resposta, pk=id_resposta)
    topico.delete()
 
    messages.info(request, 'Tópico Deletado com sucesso.')
    return redirect('/topico/view-respostas/')