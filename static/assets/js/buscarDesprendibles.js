function consultarBeneficiario() {
    let idDocumentoAfiliado = $('#idDocumentoAfiliado').val()
    $.ajax({
        data : { 
            documentoAfiliado: idDocumentoAfiliado
        },
        type : 'POST',
        url : '/desprendibleSolicitudLibranza'
    })
    .done(function(data) {
        debugger
        let ddlDesprendibles = $('#cbxDesprendiblesPagoBeneficiario')
        ddlDesprendibles.html('');
        if (data.error) {
            
            $('.error').html(data.message)
            $('.error').css('display', 'block')
        }else if(data.data.length >= 2) {
            $('#modalDesprendiblesPagoBeneficiario').modal('show')
        
            data.data.forEach(element => {
                ddlDesprendibles.append(`<option value="${element[0]}">${element[0]}</option>`)
            });
            $("#cerrarModal").click();
        }
        else {
            $(".modal-backdrop").remove();
            $("#contenido").html(data.page);
            $(".modal-backdrop").remove();
            let desprendible = data.data[0][0];
            seguir(desprendible);
            $("#cerrarModal").click();
        }
      
        
    });
}
function seguir(desprendible) {
    if (!desprendible) {
        desprendible = $('#cbxDesprendiblesPagoBeneficiario').val()
    }

    $.ajax({
        data : {
            documentoAfiliado: $('#idDocumentoAfiliado').val(),
            desprendible: desprendible
        },
        type : 'POST',
        url : '/insertarOtpSolicitudLibranza',
        success: function(response) {
            $('#modalDesprendiblesPagoBeneficiario').modal('toggle')
            $(".modal-backdrop").remove();
            $("#contenido").html(JSON.parse(response).page);  
            $(".modal-backdrop").remove();   
            $("#cerrarModal").click();  
        }
    })
}