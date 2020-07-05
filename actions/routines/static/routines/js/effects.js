//De todos los menus
function openMenu(){
    var a = document.getElementsByClassName('menu-lateral')[0];
    a.style.left = "0";

    document.body.style.overflow = "hidden";
    window.scroll({top: 0, left: 0, behavior: 'smooth' });
    //document.body.scrollTop = 0; // For Safari
    //document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
function closeMenu(){
    var a = document.getElementsByClassName('menu-lateral')[0];
    a.style.left = "-100%";

    document.body.style.overflow = "auto";
}


function showExercise(){
    var acc = document.getElementsByClassName("dia");
    var i;

    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight){
          panel.style.maxHeight = null;
        } else {
          panel.style.maxHeight = panel.scrollHeight + "px";
        }
      });
    }
}


//revisar ----> mirutina.html
$(document).ready(function(){
    var i=1;

  $("#add_row").click(function(){                                                                                                                   //<td><input type='number' ></td>
    $('#addr'+i).html("<th scope='row'>"+ (i+1) +"</th> <td><input type='number' name='rep"+ (i+1) +"' id='rep"+ (i+1) +"' min='1' max='100'></td> <td><input type='number' name='peso"+ (i+1) +"' id='peso"+ (i+1) +"' min='"+ (i+1) +"' max='100'></td>");
    $('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');
    i++;
  });

  $("#delete_row").click(function(){
    if(i>3){
          $("#addr"+(i-1)).html('');
          i--;
    }
  });

});

//mirutina.html
function cambiarSem(actual, sig){
  $('.semana'+actual).css('display', 'none');
  $('.semana'+sig).css('display', 'block');
}

// index.html
function validateUser(){
  var x = document.getElementById('emailIngreso').value;
  if(x == 'a'){
    window.open('home.html', '_self');
  }else{
    window.open('t_index.html', '_self');
  }
}

//t_index.html
function searchClient() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("listClient");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
      a = li[i].getElementsByTagName("a")[0];
      if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
          li[i].style.display = "";
      } else {
          li[i].style.display = "none";
      }
  }
}


//para todos
window.onload = function() {
  var w = window.innerWidth
  || document.documentElement.clientWidth
  || document.body.clientWidth;

  var h = window.innerHeight
  || document.documentElement.clientHeight
  || document.body.clientHeight;

  document.getElementsByClassName("contenido")[0].style.height = h+'px';
  document.getElementsByClassName("contenido")[0].style.width = w+'px';


};
