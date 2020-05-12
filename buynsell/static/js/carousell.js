document.getElementById('button').addEventListener('click',
function(){
    document.querySelector('.signup').style.display='flex';
    document.querySelector('.card-deck').style.display='none';
});

document.querySelector('.close').addEventListener('click',
function(){
    document.querySelector('.signup').style.display='none';
    document.querySelector('.card-deck').style.display='flex';
});