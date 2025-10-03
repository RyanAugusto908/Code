// libraries
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// Globals


// Functions

rl.question("Digite o número inteiro: ", num)
num = parseInt(num)
console.log(num)

function soma(num1,num2){
    console.log(num1 + num2)
}
soma(3,2)

function par_impar(num){
    if (num % 2 == 0){
        console.log(num + " é par")
    } else {
        console.log(num + " é impar")
    }
}

par_impar(9)