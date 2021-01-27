function activateCamera(){
    var video = document.querySelector("#videoElement");
  
    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            document.getElementById("welcome-content").classList.add("fadeout")
            setTimeout(()=>{
                document.getElementById("welcome-content").style.display = "none";
            }, 1000)
        }).catch(function (err0r) {
            alert('No hemos podido detectar tú cámara');
        });
    }
}
  //432 577
  activateCamera();

  function restart (){
    let img1 = document.createElement("img");
    img1.className = "screenshot-image";
    img1.style.objectFit = "cover";
    let img2 = document.createElement("img");
    img2.className = "screenshot-image";
    img2.style.objectFit = "cover";
    let img3 = document.createElement("img");
    img3.className = "screenshot-image";
    img3.style.objectFit = "cover";


    img1.id = "photo";
    img2.id = "photo2";
    img3.id = "photo3";

    document.querySelector('#photo').replaceWith( img1 );
    document.querySelector('#photo2').replaceWith( img2 );
    document.querySelector('#photo3').replaceWith( img3 );
    document.getElementById("imgB64Input1").value = "";
    document.getElementById("imgB64Input2").value = "";
    document.getElementById("imgB64Input3").value = "";

    document.getElementById("primeraCaptura").style.display = "block";
    document.getElementById("segundaCaptura").style.display = "none";
    document.getElementById("segundaCaptura").style.display = "none";
    document.getElementById("enviarRegistroFacial").style.display = "none";

  }

  function takeSnapshot() {
    //Obtiene El Video
    var video = document.querySelector("#videoElement");
  
    //Obtiene el tamaño del video
    var videoHeight = video.clientHeight; 
    var videoWidth = video.clientWidth; 
  
    //Obtiene el Canvas
    var canvas = document.getElementById('canvas');
    // Se le asigna el mismo tamaño del video
    canvas.height = videoHeight;
    canvas.width = videoWidth;
    var context = canvas.getContext('2d');
  
    //dibuja Imagen Del video en el Canvas
    context.drawImage(video, 0, 0, videoWidth, videoHeight );
    
    //Convertir en Base 64
    var data = canvas.toDataURL();
    
    //Obtiene la imagen
    var photo = document.querySelector('#photo');
    
    // Se le asigna el data
    photo.setAttribute('src', data);
    document.getElementById("imgB64Input1").value = data;

    document.getElementById("primeraCaptura").style.display = "none";
    document.getElementById("segundaCaptura").style.display = "block";
  }

  //Segundo Captura
  function takeSnapshot2() {
    //Obtiene El Video
    var video = document.querySelector("#videoElement");
  
    //Obtiene el tamaño del video
    var videoHeight = video.clientHeight; 
    var videoWidth = video.clientWidth; 
  
    //Obtiene el Canvas
    var canvas = document.getElementById('canvas');
    // Se le asigna el mismo tamaño del video
    canvas.height = videoHeight;
    canvas.width = videoWidth;
    var context = canvas.getContext('2d');
  
    //dibuja Imagen Del video en el Canvas
    context.drawImage(video, 0, 0, videoWidth, videoHeight );
    
    //Convertir en Base 64
    var data2 = canvas.toDataURL();
    
    //Obtiene la imagen
    var photo = document.querySelector('#photo2');
    
    // Se le asigna el data
    photo.setAttribute('src', data2);
    document.getElementById("imgB64Input2").value = data2;

    document.getElementById("segundaCaptura").style.display = "none";
    document.getElementById("terceraCaptura").style.display = "block";
  }

  //Tercera Captura
  function takeSnapshot3() {
    //Obtiene El Video
    var video = document.querySelector("#videoElement");
  
    //Obtiene el tamaño del video
    var videoHeight = video.clientHeight; 
    var videoWidth = video.clientWidth; 
  
    //Obtiene el Canvas
    var canvas = document.getElementById('canvas');
    // Se le asigna el mismo tamaño del video
    canvas.height = videoHeight;
    canvas.width = videoWidth;
    var context = canvas.getContext('2d');
  
    //dibuja Imagen Del video en el Canvas
    context.drawImage(video, 0, 0, videoWidth, videoHeight );
    
    //Convertir en Base 64
    var data3 = canvas.toDataURL();
    
    //Obtiene la imagen
    var photo = document.querySelector('#photo3');
    
    // Se le asigna el data
    photo.setAttribute('src', data3);
    document.getElementById("imgB64Input3").value = data3;

    document.getElementById("terceraCaptura").style.display = "none";
    document.getElementById("enviarRegistroFacial").style.display = "block";
  }

  navigator.permissions.query({name:'camera'}).then(res => {
    res.onchange = ((e)=>{
      if (e.type === 'change'){
        location.reload();
      }
    })
  })