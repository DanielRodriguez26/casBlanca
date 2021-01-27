$(document).ready(function() {
    $("#homeProducto").click(function() {
        location.reload();
    });
});

$(document).ready(function() {
    $("#liFuncionarioProducto").click(function() {
        $("#contenido").load("funcionarioProducto");
    });
});


$(document).ready(function() {
    $("#modificarDescuento").click(function() {
        $("#contenido").load("/modificarDescuentosActivosProducto", {
            ajax:'y',
            section:'request',
            idRolDescuentoProducto: $("#rolDescuentoProducto").val(),
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
    $("#funcionariosOperadorBloqueados").click(function() {
        $("#contenido").load("funcionarioOperadorBloqueado");
    });
});

$(document).ready(function() {
    $("#cambiarContrasena").click(function() {
        $("#contenido").load("cambiarContrasenaOperador");
    });
});

$(document).ready(function() {
    $("#descuentoProducto").click(function() {
        $("#contenido").load("descuentosProducto");
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
