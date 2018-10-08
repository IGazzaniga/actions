function openMenu(){
    var a = document.getElementsByClassName('menu-lateral')[0];
    a.style.left = "0";
    document.body.style.backgroundColor = "rgba(0,0,0,0.8)";
}

function closeMenu(){
    var a = document.getElementsByClassName('menu-lateral')[0];
    a.style.left = "-75%";
    document.body.style.backgroundColor = "rgba(0,0,0,0)";
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