let cor_nova = "#005000"
fon_nova = "#ff0000ff"
texto_novo = "Texto Alterado"

function alerta() {
    alert("hello World");
}

function mudar_fon(){
    let cor_antiga = document.body.style.backgroundColor
    document.body.style.backgroundColor = cor_nova
    cor_nova = cor_antiga
}
function mudar_cor(){
    let cor_antiga = document.body.style.backgroundColor
    document.body.style.backgroundColor = cor_nova
    cor_nova = cor_antiga
}

function alterar_texto(elemento) {
    let texto_antigo = elemento.innerText
    elemento.innerText = texto_novo
    texto_novo = texto_antigo
}