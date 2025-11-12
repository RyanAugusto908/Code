// Seleciona todos os elementos com a classe "carta" (as cartas do jogo)
const cards = document.querySelectorAll('.carta');

// Controla se uma carta ja foi virada
let hasFlippedCard = false;

//Impede o jogador de virar mais cartas enquanto as anteriores estão sendo verificas
let lockBoard = false;

// Armazena a primeira e a segunda carta virada
let firstCard, secondCard;

// Função para virar uma carta (chamada ao clicar)
function flipCard(){
    if(lockBoard) return; // Se o tabuleiro estiver travado, não faz nada
    if (this === firstCard) return; // Impede Clicar duas vezes na mesma carta
    this.ClassList.add('flip'); // Adiciona a classe que aplica o efeito de virar
    if (!hasFlippedCard){
        hasFlippedCard = true; // Marca que a primeira carta foi virada
        firstCard = this; // Armazena a carta atual como primeira
        return; // Sai da função e aguarda a primeira carta
    }

    // Se for a segunda carta
    secondCard = this;
    lockBoard = true; // Bloqueia o tabuleiro até verificar o par

    checkForMatch(); // Verifica se as duas cartas são iguais
}

//Função para verificar se as duas cartas viradas são um par
function checkForMatch(){
    let isMatch = firstCard.dataset.framework === secpmdCard.dataset.framework;

    //se for par, desativa as cartas, senão, desvira
    isMatch ? disableCards() : unflipCards();
}

function resetBoard(){
    [hasFlippedCard, lockBoard] = [false,false];
    [firstCard, secondCard] = [null,null];
}

(function shuffle(){
    cards.forEach(card => {
        let randomPos = Math.floor(Math.random() * 12);
        card.style.order = randomPos;
    })
})

cards.forEach(card => card.addEventListener('click', flipCard));

window.onload = function(){
    let clickDiv = document.getElementById("click-div");

    let resetBtn = document.getElementById('reset-button');

    resetBtn.onclick = resetCounter;
}

var countarVal = 0;

incrementClick = function(){
    updateDisplay(++counterVal);   
}

function resetCounter(){
    countarVal = 0;
    updateDisplay(countarVal);
}

function updateDisplay(val){
    document.getElementById("counter-label").innerHTML = val;
}