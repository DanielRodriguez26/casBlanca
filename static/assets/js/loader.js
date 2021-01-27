// Se ejecuta cuando se realiza cualquier llamado XHR
$( document ).ajaxSend(function(){
    makeLoader();
})
// Se ejecuta cuando se realiza el submit de un formulario
$( document ).ready(function(){
    $("form").submit(function(e){
        makeLoader();
    });
});
// Removemos el elemento cuando se haya completado el llamado ajax
$( document ).ajaxComplete(function() {
    $(".loader").remove();
});

// Crea y muestra el loader element
function makeLoader(){
    var loader = document.createElement("div");
    $( loader ).append(`
        <i class="fa fa-spinner fa-pulse fa-3x fa-fw  loader-spinner"></i>
    `);
    $( loader ).addClass("loader")
    document.body.insertBefore(loader, document.body.firstChild);
}