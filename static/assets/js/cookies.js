//<script src="{{url_for('static', filename ='assets/js/cookies.js')}}"></script>


$(document).ready(function () {
    compruebaAceptaCookies();
});

function compruebaAceptaCookies() {
    if (localStorage.aceptaCookies == 'true') {
        $("#modalCookie1").modal("hide")

    } else {
        $("#modalCookie1").modal("show")

    }
}

function aceptaCookies() {
    console.log(localStorage)
    localStorage.aceptaCookies = 'true'
    $("#modalCookie1").modal("hide")
    //setCookie();
}

/*
function setCookie() {
    var d = new Date();
    d.setTime(d.getTime() + (30 * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toGMTString();
    document.cookie = "name= Dibanka; " + expires + ";path=/";
}


function checkCookie() {
    var user = getCookie();
    if (user != "") {
        $("#modalCookie1").modal("hide")
    } else {
        $("#modalCookie1").modal("show")
    }
}*/