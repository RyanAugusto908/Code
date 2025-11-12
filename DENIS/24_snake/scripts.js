// === IMAGENS ===
let headImg = new Image();
headImg.src = "cobra.png"; // cabeça da cobra

let bodyImg = new Image();
bodyImg.src = "cobra_corpo.png"; // corpo da cobra

let foodImg = new Image();
foodImg.src = "comida.png"; // imagem da comida (ex: maçã, fruta, etc.)

// === CANVAS E CONFIGURAÇÃO ===
let canvas = document.getElementById("snake");
let context = canvas.getContext("2d");

// Cada "quadradinho" da grade
let box = 50;

// Tamanho do campo (10x10 blocos de 52px = 520px)
let gridSize = 20;

// Cobra: lista de posições (começa com 1 bloco)
let snake = [];
snake[0] = { x: 100 * box, y: 100 * box };

// Direção inicial
let direction = "right";

// === COMIDA ===
let food = {
  x: Math.floor(Math.random() * gridSize) * box,
  y: Math.floor(Math.random() * gridSize) * box
};

// === CONTROLE DE CARREGAMENTO DAS IMAGENS ===
let imagensCarregadas = 0;
const totalImagens = 3;
let jogo;

function verificarCarregamento() {
  imagensCarregadas++;
  if (imagensCarregadas === totalImagens) {
    jogo = setInterval(iniciarJogo, 70); // velocidade ajustada
  }
}

headImg.onload = verificarCarregamento;
bodyImg.onload = verificarCarregamento;
foodImg.onload = verificarCarregamento;

// === FUNÇÃO PARA DESENHAR O FUNDO ===
function criarBG() {
  // Fundo em gradiente suave
  const gradiente = context.createLinearGradient(0, 0, 512, 512);
  gradiente.addColorStop(0, "#aa3e00ff");
  gradiente.addColorStop(1, "#e4850aff");
  context.fillStyle = gradiente;

  // Cobre exatamente o tamanho do canvas
  context.fillRect(0, 0, 1000, 1000);
}

// === FUNÇÃO PARA DESENHAR A COBRA ===
function criarCobrinha() {
  for (let i = 0; i < snake.length; i++) {
    if (i === 0) {
      context.drawImage(headImg, snake[i].x, snake[i].y, box, box);
    } else {
      context.drawImage(bodyImg, snake[i].x, snake[i].y, box, box);
    }
  }
}

// === FUNÇÃO PARA DESENHAR A COMIDA ===
function drawFood() {
  context.drawImage(foodImg, food.x, food.y, box, box);
}

// === CONTROLE DAS SETAS ===
document.addEventListener('keydown', update);

function update(event) {
  if (event.keyCode == 65 && direction != 'right') direction = 'left';
  if (event.keyCode == 87 && direction != 'down') direction = 'up';
  if (event.keyCode == 68 && direction != 'left') direction = 'right';
  if (event.keyCode == 83 && direction != 'up') direction = 'down';
}

// === FUNÇÃO PRINCIPAL DO JOGO ===
function iniciarJogo() {
  // Fazer a cobra atravessar as bordas
  if (snake[0].x >= gridSize * box && direction == "right") snake[0].x = 0;
  if (snake[0].x < 0 && direction == "left") snake[0].x = (gridSize - 1) * box;
  if (snake[0].y >= gridSize * box && direction == "down") snake[0].y = 0;
  if (snake[0].y < 0 && direction == "up") snake[0].y = (gridSize - 1) * box;

  // Verificar colisão com o próprio corpo
  for (let i = 1; i < snake.length; i++) {
    if (snake[0].x == snake[i].x && snake[0].y == snake[i].y) {
      clearInterval(jogo);
      alert('Game Over 😢');
    }
  }

  // Atualiza o fundo, cobra e comida
  criarBG();
  criarCobrinha();
  drawFood();

  // Posição atual da cabeça
  let snakeX = snake[0].x;
  let snakeY = snake[0].y;

  // Movimento
  if (direction == "right") snakeX += box;
  if (direction == "left") snakeX -= box;
  if (direction == "up") snakeY -= box;
  if (direction == "down") snakeY += box;

  // Verifica se comeu a comida
  if (snakeX != food.x || snakeY != food.y) {
    snake.pop(); // remove o último bloco
  } else {
    // Gera nova comida dentro da grade
    food.x = Math.floor(Math.random() * gridSize) * box;
    food.y = Math.floor(Math.random() * gridSize) * box;
  }

  // Nova cabeça
  let newHead = { x: snakeX, y: snakeY };
  snake.unshift(newHead);
}
