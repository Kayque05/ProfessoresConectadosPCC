
console.log("Ola mundo");
$(document).ready(function(){
    
    var baseUrl = 'http://127.0.0.1:8000/perguntas/';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    var filter = $('#filter');
    $(filter).change(function(){
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;

    });

    $(deleteBtn).on('click', function(e){
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm("Deseja realmente deletar esta tarefa?");

        if(result){
            window.location.href = delLink;
        }
    });
    $(searchBtn).on('click', function(){
        searchForm.submit();

    });

});

//JS para a Navbar ------------------------------------------------------------------------------------------------

const btnMobile = document.getElementById('btn-mobile');

function toggleMenu(event){
    if (event.type === 'touchstart') event.preventDefault();
    const nav = document.getElementById('nav');
    nav.classList.toggle('active')
}

btnMobile.addEventListener('click', toggleMenu)
btnMobile.addEventListener('touchstart', toggleMenu)