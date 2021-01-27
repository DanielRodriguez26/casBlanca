// Home Beneficiario
$(document).ready(function() {
	$("#conceptosCrediticios").click(function() {

		var identificadorDesprendiblePago = $("#hiddenDesprendiblesPagoBeneficiario").val();
		$("#contenido").load("descuentosBeneficiarios/" + identificadorDesprendiblePago);
	});

	$("#btnConsultarDesprendiblesPagoBeneficiario").click(function() {

		var identificadorDesprendiblePago = $("#cbxDesprendiblesPagoBeneficiario").val();
		$("#contenido").load("descuentosBeneficiarios/" + identificadorDesprendiblePago);
		$("#btnCerrarModalDesprendiblesPagoBeneficiario").click();
		 
	});

	$("#cambiarContrasena").click(function() {
		$("#contenido").load("cambiarContrasenaBeneficiario");
	});

	$("#inicioBeneficiario").click(function() {
	location.reload();
	})

	$("#adelantoNomina").click(function() {
		$("#contenido").load("adelantoNomina");
	})

	$("#documentosSolicitados").click(function() {
		$("#contenido").load("documentosSolicitadosBeneficiario");
	})
	
	$("#perfilBeneficiario").click(function() {
		$("#contenido").load("perfilBeneficiarioNew");
	});

	$("#solicitarDocumentos").click(function() {
		$("#contenido").load("solicitarDocumentos");
	});

	$("#prueba").click(function() {
		$("#contenido").load("prueba");
	});;

//Fin Home Beneficiario

// Libranza
	$("#volverLibranza").click(function() {
		var identificadorDesprendiblePago = $("#txtDesprendible").attr('placeholder');
		$("#contenido").load("descuentosBeneficiarios/"+identificadorDesprendiblePago);
	});

//anticipo
	$("#continuar").click(function() {
		$("#contenido").load("adelantoNominaSimulado");
    });
    
    //HugoS:10-Dic-2020 rutas home menu
    $("#manualUsuario").click(function() {
        window.open("https://bit.ly/34BZwt4", "_blank");
	});
	$("#directorio").click(function() {
        window.open("https://aliadosfinancieros.online/", "_blank");
    });
    $("#logout").click(function() {
        if (!confirm('¿Está seguro que desea cerrar sesión?')) return;
        window.location.href = "/logout";
    });
});
