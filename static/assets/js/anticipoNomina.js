$(document).ready(function() {
    $("#simularAdelanto").click(function(){
        var cupo = document.getElementById("cupoDisponible").value;
        var cupo= parseInt(cupo);
        
        var montoIngresado= document.getElementById("montoAnticipo").value;
        var montoAnticipo= parseInt(montoAnticipo);

        var plazoAnticipo= document.getElementById("plazoAnticipo").value;
        var plazoAnticipo= parseInt(plazoAnticipo);
        
        var montoMaximoAnticipo2Mes = cupo*2;
        var montoMaximoAnticipo3Mes = cupo*3;

        if (cupo>=montoIngresado){
            $.ajax({
                data : { 
                    montoAnticipo : $('#montoAnticipo').val(),
                    plazoAnticipo
                },
                type : 'POST',
                url : '/adelantoNominaSimulado'
            })
            .done(function(data) {
                $("#simulacionAnticipo").load("/adelantoNominaSimulado");
            });
        }

        else if ( montoMaximoAnticipo2Mes>= montoIngresado && plazoAnticipo==2){
            $.ajax({
                data : { 
                    montoAnticipo : $('#montoAnticipo').val(),
                    plazoAnticipo
                },
                type : 'POST',
                url : '/adelantoNominaSimulado'
            })
            .done(function(data) {
                $("#simulacionAnticipo").load("/adelantoNominaSimulado");
            });
        } 

        else if (montoMaximoAnticipo3Mes>= montoIngresado && plazoAnticipo==3){
            $.ajax({
                data : { 
                    montoAnticipo : $('#montoAnticipo').val(),
                    plazoAnticipo
                },
                type : 'POST',
                url : '/adelantoNominaSimulado'
            })
            .done(function(data) {
                $("#simulacionAnticipo").load("/adelantoNominaSimulado");
            });
        }
        
        else if (montoMaximoAnticipo3Mes>= montoIngresado && plazoAnticipo<3){
            alert("El monto solicitado excede su capacidad mensual, por favor incremente el plazo")
        }
        else if (montoMaximoAnticipo3Mes< montoIngresado ){
            alert("El monto solicitado excede su monto maximo de anticipo, por favor reduzca el monto solicitado e intente de nuevo ")
        }
        event.preventDefault();   
    });
});