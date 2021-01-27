function activateCamera(){
    var video = document.querySelector("#videoElement");

    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
        })
        .catch(function (err0r) {
            console.log("Something went wrong!");
        });
    }
}
function restart (){
    let img = document.createElement("img");
    img.className = "screenshot-image";
    img.style.objectFit = "cover";


    img.id = "photo";

    document.querySelector('#photo').replaceWith( img );
    document.getElementById("imgB64Input").value = "";

    document.getElementById("primeraCaptura").style.display = "block";
    document.getElementById("validarRegistroFacial").style.display = "none";
  }

//432 577
activateCamera();

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
    document.getElementById("imgB64Input").value = data;

    document.getElementById("primeraCaptura").style.display = "none";
    document.getElementById("validarRegistroFacial").style.display = "block";
}