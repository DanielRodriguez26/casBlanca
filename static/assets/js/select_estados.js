$(document).ready(function () {
    // Cargamos los estados
    var estados = "<option value='' disabled selected>Selecciona el departamento</option>";

    for (var key in municipios) {
        if (municipios.hasOwnProperty(key)) {
            estados = estados + "<option value='" + key + "'>" + key + "</option>";
        }
    }

    $('#estado').html(estados);

    // Al detectar
    $("#estado").change(function () {
        var html = "<option value='' disabled selected>Selecciona el municipio</option>";
        $("#estado option:selected").each(function () {
            var estado = $(this).text();
            if (estado != "Selecciona el departamento") {
                var municipio = municipios[estado];
                if (municipio) {
                    for (var i = 0; i < municipio.length; i++)
                        html += "<option value='" + municipio[i] + "'>" + municipio[i] + "</option>";
                }
            }
        });
        $('#municipio').html(html);
    })
        .trigger("change");
});