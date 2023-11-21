
       
 function move() {

  var elem = document.getElementById("myBar");
  var width = 1;
  var id = setInterval(frame, 1000);
  
  function frame() {
    
    if (width >= 100) {
       
      clearInterval(id);
      document.getElementById("myBar").style.display = "none";
      alert("success")
    } else {
      width++;
      elem.style.width = width + '%';
      
    }

    
}


}
  
           
        
    
