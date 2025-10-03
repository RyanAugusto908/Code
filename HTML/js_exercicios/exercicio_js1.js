function soma(){
    let s_a = parseInt(document.getElementById("a").value)
    let s_b = parseInt(document.getElementById("b").value)

    let soma = s_a + s_b
    document.getElementById("total").innerHTML = soma
    console.log(soma)
}

function par_impar(){
    let p_i_number1 = parseInt(document.getElementById("p_i_number1").value)
    if (p_i_number1 % 2 == 0) {
        document.getElementById("p_i_resultado").innerText = "par"
    } else {
        document.getElementById("p_i_resultado").innerText = "impar"
    }
}

function comparar(){
    let comp_a = parseInt(document.getElementById("comp_a").value)
    let comp_b = parseInt(document.getElementById("comp_b").value)

    if (comp_a < comp_b) {
        document.getElementById("comp_resultado").innerText = "Menor"
    } else {
        document.getElementById("comp_resultado").innerText = "Maior"        
    }
}