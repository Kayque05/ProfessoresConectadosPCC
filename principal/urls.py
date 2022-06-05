from django.urls import path
from . import views

#URLS concetando as views ao template
urlpatterns = [
    path('', views.telahome, name='principal-temp'),

    #Aqui mostra todas as perguntas frequentes.
    path('Perguntas/', views.Pergunta, name='Perguntas_Frequentes'),
    #Detalhar a visualização de uma pergunta
    path('Perguntas/detalhe/<int:id>', views.detailPerguntas, name='pergunta_detail'),

################### Topicos ###########################################

    #Listar Tópico
    path('Topico/', views.PaginaTopicos, name='Topico'),

    #Adicionar tópico
    path('Topico/add-topico/', views.novoTopico, name='Adicionar-Topico'),
    #Detalhar Tópico
    path('Topico/Detalhe/<int:id_topico>', views.viewTopico, name='topico'),
   

    #Visualizar Tópico por usuário logado
    path('Topico/view-topicos/', views.meusTopicos, name='MeusTopicos'),
    #Editar Tópico
    path('Topico/view-topicos/editTopico/<int:id_topico>', views.editTopico, name='editar-Topico'),
    #Deletar topico
    path('Topico/view-topicos/delete/<int:id_topico>', views.deletarTopico, name='Deletar-Topico'),
    
################## Comentários #########################################

    #esta Url vai adicionar uma Resposta
    path('Topico/add/<int:id>', views.addResposta, name='addRomentario' ),
    #visualizar MinhasRespostas
    path('Topico/view-respostas/', views.minhasRespostas, name='viewRespost'),
    #Editar Resposta
    path('Topico/view-respostas/editResposta/<int:id_resposta>', views.editResposta, name='editResposta'),
    #Deletar Resposta
    path('Topico/view-respostas/delete/<int:id_resposta>', views.deletarResposta, name='DeletarResposta'),
################## Conteúdos ############################################

    #Listar Conteúdos
    path('listar/<int:conteudo_id>', views.listarConteudo, name='listarConteudo'),
    path('listar/material/<int:id>', views.listarMaterial, name='list'),




    ##path('acessacurso/<int:id>', views.acessarCurso, name="cursos-google"),
    ##path('acessacurso/PerguntaCurso/<int:id>', views.detailPerguntas, name="detail-perguntas"),
    #path('acessagoogle/faqgoogle/', views.forum, name="faq-google"),
    #path('acessagoogle/faqgoogle/edit/<int:id>', views.editTask, name="edit-task"),
   # path('acessagoogle/faqgoogle/newtopico/', views.newtopico, name="novo-topico"),
   # path('acessagoogle/faqgoogle/viewtopic/<int:id>', views.viewTopico, name="Visualizar-Topico"),
   # path('acessagoogle/faqgoogle/deletarFaq/<int:id>', views.deletarFaq, name="deletar-faq"),
   # path('comenta/deletarcomentario/<int:id>', views.deletarComentario, name="deletar-comentario"),
]