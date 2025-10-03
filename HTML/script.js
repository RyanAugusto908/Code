function soma(){
    var valor1 = document.getElementById("num1").value;

    var valor2 = document.getElementById("num2").value;

    var total = parseInt(valor1) + parseInt(valor2);

    document.getElementById("total").innerHTML = "O resultado é: " + total;
}
function par(){
    var x,texto;

    x = document.getElementById("numero").value

    if (x % 2 == 0){
        texto = "O número é par";
    } else {
        texto = "O número é impar";
    }

    document.getElementById("resultado").innerHTML = texto;
}

function converterCelsiusParaFahrenheit(){
    
    const celsius = document.getElementById("celsius").value;

    const fahrenheit = (celsius * 9/5) + 32;

    document.getElementById("resultado2").innerHTML = "A conversão para fahrenheit é: " + fahrenheit;
}