$(document).ready(function() {
    $("#homePriorizado").click(function() {
        location.reload();
    });
});

$(document).ready(function() {
    $("#modificarDescuento").click(function() {
        $("#contenido").load("/modificarDescuentosActivosPriorizado", {
            ajax:'y',
            section:'request',
            idValueDescuentoPriorizado: $("#rolDescuentoPriorizado").val(),
         }, function(response, status, xhr) {
         });

         $("#cerrarModal23").click()
    });
});

$(document).ready(function() {
    $("#codigos").click(function() {
        $("#contenido").load("conceptosActivosOperador");
    });
});

$(document).ready(function() {
    $("#funcionariosPriorizado").click(function() {
        $("#contenido").load("funcionarioPriorizado");
    });
});

$(document).ready(function() {
    $("#funcionariosPriorizadoBloqueados").click(function() {
        $("#contenido").load("funcionarioOperadorBloqueado");
    });
});

$(document).ready(function() {
    $("#crearUsuario").click(function() {
        $("#contenido").load("agregarFuncionario2");
    });
});

$(document).ready(function() {
    $("#cambiarContrasena").click(function() {
        $("#contenido").load("cambiarContrasenaOperador");
    });
});

$(document).ready(function() {
    $("#descuentoPriorizado").click(function() {
        $("#contenido").load("descuentosPriorizado");
    });

    //HugoS:10-Dic-2020 rutas home menu
    $("#manualUsuario").click(function() {
        window.open("https://bit.ly/3kU3gLh", "_blank");
    });
    $("#logout").click(function() {
        if (!confirm('¿Está seguro que desea cerrar sesión?')) return;
        window.location.href = "/logout";
    });
});
