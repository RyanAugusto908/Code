function calcularIMC() {
    let peso = parseFloat(document.getElementById("peso").value);
    let altura = parseFloat(document.getElementById("altura").value);

    let imc = peso / (altura * altura);
    let classificacao = "";

    if (imc < 18.5) {
    classificacao = "MAGRISSIMO";
    } else if (imc < 25) {
    classificacao = "Peso normal";
    } else if (imc < 30) {
    classificacao = "Sobrepeso";
    } else if (imc < 35) {
    classificacao = "Obesidade grau 1";
    } else if (imc < 40) {
    classificacao = "Obesidade grau 2";
    } else {
    classificacao = "Obesidade grau 3";
    }

    document.getElementById("resultado").innerText = 
    "Seu IMC é " + imc.toFixed(2) + " (" + classificacao + ")";
}