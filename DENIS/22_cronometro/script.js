let tempoInicialCrescente = 0;
let tempoInicialDecrescente = 10;
let jogoAtivoDecrescente = false;
let jogoAtivoCrescente = false
let tempoRestante = tempoInicial;

function crescente() {
    jogoAtivoCrescente = true
    if (jogoAtivoCrescente == true) {
        atualizarTempoCrescente();
        setTimeout(() => {
            crescente();
        }, 1000);
    }

}

function atualizarTempoCrescente() {
    tempoInicialCrescente++;
    document.getElementById("tempo").textContent = `Tempo: ${tempoInicialCrescente}s`;
}

function decrescente() {
    atualizarTempoDecrescente();
    jogoAtivoDecrescente = true
    setTimeout(() => {
        decrescente();
    }, 1000);

    if (jogoAtivoCrescente == true) {
        jogoAtivoDecrescente = false;
    }
}

function atualizarTempoDecrescente() {
    tempoInicialDecrescente--;
    document.getElementById("tempo").textContent = `Tempo: ${tempoInicialDecrescente}s`;
}