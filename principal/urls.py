from django.urls import path
from . import views

#URLS concetando as views ao template
urlpatterns = [
    path('', views.telahome, name='principal-temp'),

    #Aqui adiciona um curso
    path('add-curso/', views.addCurso, name="add-curso"),
    #Aqui Deleta um curso
    path('deleteCurso/<int:id_curso>', views.deletarCurso, name="delete-curso"),
    #Aqui Edita um curso
    path('editCurso/<int:id_curso>', views.editCurso, name="edit-curso"),

############### Conteudo #####################

    #Adcionar Conteudo
    path('add-conteudo/<int:id_conteudo>', views.addConteudo, name="add-conteudo"),
    #Deletar Conteudo
    path('deletarConteudo/<int:id_conteudo>', views.deletarConteudo, name="deletarConteudo"),
    #Editar Conteudo
    path('editarConteudo/<int:id_conteudo>', views.editConteudo, name="editarConteudo"),


################# FAQ ##################
    path('perguntas/', views.Pergunta, name='Perguntas_Frequentes'),
    #Detalhar a visualização de uma pergunta
    path('perguntas/detalhe/<int:id>', views.detailPerguntas, name='pergunta_detail'),

    #adicionar pergunta frequente
    path('perguntas/add-faq/', views.addPerguntaFrequente, name='Add_Perguntas_Frequentes'),

    #Editar Pergunta Frequente
    path('perguntas/edit-faq/<int:id_pergunta>', views.editPerguntasFrequentes, name='edit_Perguntas_Frequentes'),
    #Deletar Pergunta Frequente
    path('perguntas/delete-faq/<int:id_pergunta>', views.deletarPergunta, name='Delete_Perguntas_Frequentes'),
################### Topicos ###########################################

    #Listar Tópico
    path('topico/', views.PaginaTopicos, name='Topico'),

    #Adicionar tópico
    path('topico/add-topico/', views.novoTopico, name='Adicionar-Topico'),
    #Detalhar Tópico
    path('topico/Detalhe/<int:id_topico>', views.viewTopico, name='topico'),
   

    #Visualizar Tópico por usuário logado
    path('topico/view-topicos/', views.meusTopicos, name='MeusTopicos'),
    #Editar Tópico
    path('topico/view-topicos/editTopico/<int:id_topico>', views.editTopico, name='editar-Topico'),
    #Deletar topico
    path('topico/view-topicos/delete/<int:id_topico>', views.deletarTopico, name='Deletar-Topico'),
    
################## Comentários #########################################

    #esta Url vai adicionar uma Resposta
    path('topico/add/<int:id>', views.addResposta, name='addRomentario' ),
    #visualizar MinhasRespostas
    path('topico/view-respostas/', views.minhasRespostas, name='viewRespost'),
    #Editar Resposta
    path('topico/view-respostas/editResposta/<int:id_resposta>', views.editResposta, name='editResposta'),
    #Deletar Resposta
    path('topico/view-respostas/delete/<int:id_resposta>', views.deletarResposta, name='DeletarResposta'),
################## Conteúdos ############################################

    #Listar Conteúdos
    path('listar/<int:conteudo_id>', views.listarConteudo, name='listarConteudo'),

################# Material ########################
    #Listar Conteudo
    path('listar/conteudo/<int:id>', views.VisualizarConteudo, name='list'),
   

]