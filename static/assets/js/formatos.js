function onlyNumbers(e){
    var key= e.keycode || e.which;
    var teclado = String.fromCharCode(key);
    var numeros="0123456789";
    var especiales="8-37-38-46";
    var teclado_especial=false;
    for(var i in especiales){

        if(key == especiales[i]){
            teclado_especial=true;
        }
    }
    if(numeros.indexOf(teclado)== -1 && !teclado_especial){
        return false;
    }

}

function onlyNumbersOnPaste(e) {
    var reg = new RegExp('^[0-9]+$');
    let paste = (e.clipboardData || window.clipboardData).getData('text');
    return reg.test(paste);
}

function onlyLetters(e){
    
    key= e.keycode || e.which;
    teclado= String.fromCharCode(key).toLowerCase();
    letras= " abcdefghijklmnopqrstuvwxyzáéíóú";
    especiales="8-37-38-46-164"

    teclado_especial=false

    for(var i in especiales){
        if(key == especiales[i]){
            teclado_especial=true;break;
        }
    }
    if(letras.indexOf(teclado) == -1 && !teclado_especial){
        return false;
    }
}

function noSpecialCharacter(e) {
    var regex = new RegExp("^[a-zA-Z0-9-ZñÑ# ]+$");
    var key = String.fromCharCode(!e.charCode ? e.which : e.charCode);
    if (!regex.test(key)) {
       e.preventDefault();
       return false;
    }
}