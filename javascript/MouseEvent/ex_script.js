function soma_caixa() {
    let number1 = parseFloat(document.getElementById("caixa1").value) 
    let number2 = parseFloat(document.getElementById("caixa2").value)

    const resultado = number1 + number2
    document.getElementById("resultado").innerText = resultado
}