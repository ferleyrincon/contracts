// JAVASCRIPT FOR CONTRACTS

function next_screen(){
    document.getElementById('controlClick').value += " ]";
    document.getElementById('arrayTime').value += " ]";
    formulario = document.getElementById("form");
    formulario.submit();
}

function countdown(){
    b_countdown = document.getElementById("countdown");
    div_counter = document.getElementById("counter-time");
    time += 1;
    b_countdown.innerHTML = 10 - time;
    if(time >= 6){
        div_counter.style.backgroundColor = "#ffff66";
    }
    if(time >= 10){
        div_counter.style.backgroundColor = "#ff6666";
        next_screen();
    }
}

$(document).ready(function () {
    $('.form-check-input').click(
        function () {
        	dateClick = Date.now();
        	var timeClick = (dateClick - dateInit)/1000;
        	inputTimeClick = document.getElementById('timeClick');
        	inputTimeClick.value = timeClick;

            var valor = $('input:radio:checked').val();
            inputControlClick = document.getElementById('controlClick');
            var vi = inputControlClick.value;
            inputControlClick.value = vi + " " + valor;
            arrayTimeClick = document.getElementById('arrayTime');
            var vt = arrayTimeClick.value;
            arrayTimeClick.value = vt + " " + timeClick;
        }
    );
});

