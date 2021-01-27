$(document).ready(function() {
    $("#homeOperador").click(function() {
    
        $("#contenido").load("bienvenidaHome");
    });
});

$(document).ready(function() {
    $("#solicitudesCredito").click(function() {
        $("#contenido").load("consultarSolicitudesCredito");
    });
});

$(document).ready(function() {
    $("#codigos").click(function() {
        $("#contenido").load("conceptosActivosOperador");
    });
});

$(document).ready(function() {
    $("#solicitudDocumentosOperador").click(function() {
        $("#contenido").load("solicitudDocumentosOperador");
    });
});

$(document).ready(function() {
    $("#carteraOperador").click(function() {
        $("#contenido").load("carteraOperador");
    });
});


$(document).ready(function() {
    $("#cambiarContrasena").click(function() {
        $("#contenido").load("cambiarContrasenaOperador");
    });
});

$(document).ready(function() {
    $("#informacionUsuario").click(function() {
        $("#contenido").load("editarPerfilOperador");
    });
});

$(document).ready(function() {
    $("#funcionariosOperador").click(function() {
        $("#contenido").load("funcionarioOperador");
    });
});

$(document).ready(function() {
    $("#funcionariosOperadorBloqueados").click(function() {
        $("#contenido").load("funcionarioOperadorBloqueado");
    });
});

$(document).ready(function() {
    $("#perfilOperador").click(function() {
        $("#contenido").load("perfilOperador");
    });
});

$(document).ready(function() {
    $("#crearUsuario").click(function() {
        $("#contenido").load("agregarFuncionario2");
    });
});
$(document).ready(function() {
    $("#actualizarValores").click(function() {
        $("#contenido").load("actualizarValoresOperador");
    });
});

$(document).ready(function() {
    $("#carteras").click(function() {
        $("#contenido").load("seleccionRetiroDescuento");
    });
});
// Nuevos Modulos

$(document).ready(function() {
    $("#desactivarDescuentos").click(function() {
        $("#contenido").load("desactivarDescuentosOperador", {
            ajax:'y',
            section:'request',
            idValueDescuento: $("#rolDescuentos").val(),
         }, function(response, status, xhr) {
         });

         $("#cerrarModal2").click()
    });
});

//Solicitud de credito
$(document).ready(function() {
    $("#volverSolicitudes").click(function() {
        $("#contenido").load("consultarSolicitudesCredito");
    });
});


//Consultar Operaciones - Aholguin:29-Jul-2020
$(document).ready(function() {
    $("#consultarOperacionesOperador").click(function() {
        $("#contenido").load("consultarOperaciones");
    });
});

//Aholguin:03-Sept-2020
$(document).ready(function() {
    $("#consultarAuditoriasOperador").click(function() {
        $("#contenido").load("auditoriaOperador");
    });
});

//informes

$(document).ready(function() {
    $("#informe1").click(function() {
        $("#contenido").load("creditosDesembolsadosOperador");
    });
});
$(document).ready(function() {
    $("#informe2").click(function() {
        $("#contenido").load("tiemposRespuestaOperador");
    });
});
$(document).ready(function() {
    $("#informe3").click(function() {
        $("#contenido").load("causalesNoIncorporacionOperador");
    });
});

$(document).ready(function() {
    $("#informe4").click(function() {
        $("#contenido").load("historicoOperacionesAprobadas");
    });
});
$(document).ready(function() {
    $("#informe5").click(function() {
        $("#contenido").load("historicoOperacionesRechazadas");
    });
});
$(document).ready(function() {
    $("#informe6").click(function() {
        $("#contenido").load("historicoOperacionesAnuladas");
    });
});
$(document).ready(function() {
    $("#informe7").click(function() {
        $("#contenido").load("historicoOperacionesDesembolsadas");
    });
});

$(document).ready(function() {
    $("#btnOperacionesPeriodo").click(function() {
        $("#contenido").load("consultarOperacionesPeriodo", {
            ajax:'y',
            section:'request',
            idConcepto: $("#cbxOperacionesPeriodo").val(),
         }, function(response, status, xhr) {
         });

         $("#cerrarModalOperacionesPeriodo").click()
    });
});

$(document).ready(function() {
    $("#historialOperaciones").click(function() {
        $("#contenido").load("historialOperaciones");
    });
});  
//Aholguin:20-Octu-2020
$(document).ready(function() {
    $("#InformesCierre").click(function() {
        $("#contenido").load("InformesCierre");
    });
});  

//Aholguin:03-Sept-2020
$(document).ready(function() {
    $("#consultarAuditoriasOperador").click(function() {
        $("#contenido").load("auditoriaOperador");
    });
});

$(document).ready(function() {
    //HugoS:10-Dic-2020 rutas home menu
    $("#reporteAuditoriaOperador").click(function() {
        $("#contenido").load("reporteAuditoriaOperador");
    });
    $("#manualUsuario").click(function() {
        window.open("https://bit.ly/32TP5iB", "_blank");
    });
    $("#logout").click(function() {
        if (!confirm('¿Está seguro que desea cerrar sesión?')) return;
        window.location.href = "/logout";
    });
});

$(document).ready(function() {
    $("#estadosCompraCartera").click(function() {
        $("#contenido").load("estadosCompraCartera");
    });
    $("#btnConsultarDescuentosRetirados").click(function() {
        $("#contenido").load("consultarDescuentosOperadorRetirados", {
            ajax:'y',
            section:'request',
            idConcepto: $("#cbxCodigosRetiradosOperador").val(),
         }, function(response, status, xhr) {
         });

         $("#btnCerrarModalDescuentosRetirados").click()
    });
});

$(document).ready(function() {
    $("#continuidadDescuento").click(function() {
        $("#contenido").load("terminosYCondicionesContinuidadDescuentos");
    });
});
