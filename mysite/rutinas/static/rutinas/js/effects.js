function openMenu(){
  var a = document.getElementsByClassName('menu-lateral')[0];
  a.style.left = "0";
}

function closeMenu(){
  var a = document.getElementsByClassName('menu-lateral')[0];
  a.style.left = "-75%";
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


//revisar
$(document).ready(function(){
  var i=3;
  
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


function cambiarSem(actual, sig){
$('.semana'+actual).css('display', 'none');
$('.semana'+sig).css('display', 'block');
}