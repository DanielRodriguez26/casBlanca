$(document).ready(function() {
    $("#homeEntidad").click(function() {
        $("#contenido").load("bienvenidaHome");
    });
});
    $(document).ready(function() {
    $("#crudLibranzaEntidad").click(function() {
        $("#contenido").load("libranzaEntidad");
    });
});
$(document).ready(function() {
    $("#consultarCodigosActivos").click(function() {
        $("#contenido").load("consultarCodigosActivos")
    });
});
    $(document).ready(function() {
    $("#consultarAnticiposBeneficiarioEntidad").click(function() {
        $("#contenido").load("consultarAnticiposBeneficiarioEntidad");
    });
});
$(document).ready(function() {
    $("#consultarLibranzaBeneficiarioEntidad").click(function() {
        $("#contenido").load("consultarLibranzaBeneficiarioEntidad");
    });
});
$(document).ready(function() {
    $("#consultarOperadoresEntidad").click(function() {
        $("#contenido").load("consultarOperadoresEntidad");
    });
});
$(document).ready(function() {
    $("#perfilBeneficiarioEntidad").click(function() {
        $("#contenido").load("verPerfilBeneficiario");
    });
});

$(document).ready(function() {
    $("#registrarEmbargos").click(function() {
        $("#contenido").load("registrarEmbargos");
    });
});

$(document).ready(function() {
    $("#cambiarContrasena").click(function() {
        $("#contenido").load("cambiarContrasenaOperador");
    });
});

$(document).ready(function() {
    $("#bloqueo2AfiliadoEntidad").click(function() {
        $("#contenido").load("bloqueo2AfiliadoEntidad");
    });
});   

$(document).ready(function() {
    $("#bloqueo2OperadorEntidad").click(function() {
        $("#contenido").load("bloqueo2OperadorEntidad");
    });
});  

$(document).ready(function() {
    $("#documentosReportados").click(function() {
        $("#contenido").load("documentosReportados");
    });
});  

$(document).ready(function() {
    $("#funcionariosEntidad").click(function() {
        $("#contenido").load("funcionariosEntidad");
    });
});  

$(document).ready(function() {
    $("#funcionariosEntidadBloqueados").click(function() {
        $("#contenido").load("funcionariosEntidadBloqueados");
    });
});  

$(document).ready(function() {
    $("#historicosEntidad").click(function() {
        $("#contenido").load("historicosEntidad");
    });
});  

$(document).ready(function() {
    $("#informe1").click(function() {
        $("#contenido").load("creditosDesembolsadosEntidad");
    });
});
$(document).ready(function() {
    $("#informe2").click(function() {
        $("#contenido").load("tiemposRespuestaEntidad");
    });
});
$(document).ready(function() {
    $("#informe3").click(function() {
        $("#contenido").load("causalesNoIncorporacion");
    });
});
$(document).ready(function() {
    $("#auditoria").click(function() {
        $("#contenido").load("auditoria");
    });
    //HugoS:10-Dic-2020 rutas home menu
    $("#manualUsuario").click(function() {
        window.open("https://bit.ly/36rajqH", "_blank");
    });
    $("#logout").click(function() {
        if (!confirm('¿Está seguro que desea cerrar sesión?')) return;
        window.location.href = "/logout";
    });
});