$(document).ready(function() {
    $("#homePorductos").click(function() {
        $("#contenido").load("homePorductos");
    });
});
$(document).ready(function() {
    $("#ingresoProductos").click(function() {
        $("#contenido").load("ingresoProductos");
    });
});
$(document).ready(function() {
    $("#gastos").click(function() {
        $("#contenido").load("gastos");
    });
});
$(document).ready(function() {
    $("#cortecias").click(function() {
        $("#contenido").load("cortecias");
    });
});
$(document).ready(function() {
    $("#detallesFactura").click(function() {
        $("#contenido").load("detallesFactura");
    });
});
$(document).ready(function() {
    $("#usuarios").click(function() {
        $("#contenido").load("usuarios");
    });
});
$(document).ready(function() {
    $("#logout").click(function() {
        if (!confirm('¿Está seguro que desea cerrar sesión?')) return;
        window.location.href = "/logout";
    });
});