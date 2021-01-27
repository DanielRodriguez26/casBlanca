//Inicio del simulador




// Simulador Monto y cuota
$(document).ready(function() {

    $("#plazoCuota").click(function(){

		var checkBox = document.getElementById("checkCartera{{cartera.0}}");
		
		if (checkBox.checked == true){
			var cartera=1;
		  }
		else{
			var cartera=0;
		}

        var valorCuota= document.getElementById("valorCuota").value;
        var valorCuota= parseInt(valorCuota);

        var cupoDisponible = document.getElementById("cupoDisponible").value;
        cupoDisponible= parseInt(cupoDisponible);
        if(valorCuota <= cupoDisponible){ 

		$.ajax({
			data : { 
				cartera,
                valorCuota : $('#valorCuota').val(),
                numeroCuotas : $('#numeroCuotas').val(),
                cupoDisponible: $('#cupoDisponible').val()
			},
			type : 'POST',
			url : '/simulacionPlazoCuota'
		})
		.done(function(data) {
            $("#parrilla").load("/simulacionPlazoCuota");

		}); }
        else{
            alert("El valor de la cuota debe ser menor al cupo disponible")
        }
		event.preventDefault();

	});

    $("#plazoMonto").click(function(){

		var checkBox = document.getElementById("checkCartera{{cartera.0}}");
		
		if (checkBox.checked == true){
			var cartera=1;
		  }
		else{
			var cartera=0;
		}

		$.ajax({
			data : { 
                monto : $('#monto').val(),
                numeroCuotas : $('#numeroCuotas').val(),
                cupoDisponible: $('#cupoDisponible').val()
			},
			type : 'POST',
			url : '/simulacionPlazoMonto'
		})
		.done(function(data) {
            $("#parrilla").load("/simulacionPlazoMonto");

		}); 
		event.preventDefault();

	});
});
