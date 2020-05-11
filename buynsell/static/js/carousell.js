$(document).ready(function(){
    $('#s-button').click(function(){
        $(this).hide();
        $('#search-overtake').slideFadeToggle();
    });
});

window.onclick = function(event){
    if(event.target == document.getElementById('search-overtake')){
        document.getElementById('search-overtake').style.display = 'none';
        $('s-button').show()
    }

}