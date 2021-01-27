$(document).ready(function() {
    idleTime = 0;
    //Increment the idle time counter every minute.
    var idleInterval = setInterval(timerIncrement, 60000);
    var idTimeOutLogOut;
    var tempoInterval;
    var timer = "1:01";

    function timerIncrement() {
        idleTime++;
        if (idleTime == 5) {

            doLogout();
        }
    }
    //Zero the idle timer on mouse movement.
 
    $(this).mousemove(function(e) {
       idleTime = 0;
       clearTimeout(idTimeOutLogOut);
        timer = "1:01";
    });

    //Zero the idle timer on keypress.
 
    $(this).keypress(function(e) {
       idleTime = 0;
       clearTimeout(idTimeOutLogOut);
       timer = "1:01";
    });

    function doLogout() {
        clearInterval(tempoInterval);
        tempoInterval = setInterval(()=>{
            let tempo = timer.split(':');
            //by parsing integer, I avoid all extra string processing
            let minutes = parseInt(tempo[0], 10);
            let seconds = parseInt(tempo[1], 10);
            --seconds;
            minutes = (seconds < 0) ? --minutes : minutes;
            seconds = (seconds < 0) ? 59 : seconds;
            seconds = (seconds < 10) ? '0' + seconds : seconds;
            //minutes = (minutes < 10) ?  minutes : minutes;
            $('.countdown').html(minutes + ':' + seconds);
            timer = minutes + ':' + seconds;
        }, 1000);

        $('#alertModal').modal({
            backdrop: true,
            keyboard: true,
            show: true
        });
        // alert("Hola, ¿hay alguien ahi?, hemos cerrado su sesión por inactividad por favor vuelva a iniciar sesión ")
        // document.location.href="/logout";
        idTimeOutLogOut = setTimeout(() => {
            clearInterval(idleInterval);
            document.location.href="/logout";
        }, 60000*1);
    }

    $('body').append(
        `
        <div id="alertModal" class="modal" tabindex="-1" role="dialog">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Hola, ¿hay alguien ahí?, por su serguridad vamos a cerrar su sesión en <strong class="countdown">00:00</strong>. Haga clic en "Aceptar" para continuar conectado.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-primary" data-dismiss="modal" aria-label="Close">Aceptar</button>
                </div>
                </div>
            </div>
        </div>
        `
    );
 })