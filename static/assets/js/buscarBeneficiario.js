$(document).ready(function() {
    $("#buscarUsuario").submit(function(){
        $.ajax({
            
            data : { 
                documentoAfiliado: $('#documentoAfiliado').val()
            },
            type : 'POST',
            url : '/insertarOtpSolicitudLibranza'
        })
        .done(function(data) {
            $(".modal-backdrop").remove();
            $("#contenido").html(data);
            $(".modal-backdrop").remove();
            $("#cerrarModal").click();
        });
        event.preventDefault();
    });
});

function desprendibles(){
    $.ajax({
            
        data : { 
            documentoAfiliado: $('#documentoAfiliado').val()
        },
        type : 'POST',
        url : '/desprendibleSolicitudLibranza'
    })
    .done(function(data) {
        $("#modalDesprendiblesPagoBeneficiario").modal("show");

        // $(".modal-backdrop").remove();
        // $("#contenido").html(data);
        // $(".modal-backdrop").remove();
        // $("#cerrarModal").click();
    }); 
}