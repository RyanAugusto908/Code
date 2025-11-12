    
    /// <h1 id="criar_matriz">Criar Matriz</h1>
    const material_escolar = ["lapis","caneta"];
    document.getElementById("criar_matriz").innerHTML = "Matriz criada: " + material_escolar;

    /// <h1 id="inserir10">Inserir 10 itens</h1>
    material_escolar.push("caderno","borracha","estojo","regua","apontador","fichario","cartolina","fita","cola_quente","notebook");
    document.getElementById("inserir10").innerHTML = "Os itens adicionados na matriz 'material_escolar' são: " + material_escolar; 

    /// <h1 id="selecionar7">Selecionar item 7 da matriz</h1>
    document.getElementById("selecionar_item_7").innerHTML = "O item 7 da matriz é: "+ material_escolar[8] +".";

    /// <h1 id="inserir2">Colocar mais 2 itens</h1>
    material_escolar.push("mouse","teclado");
    document.getElementById("inserir2").innerHTML = "A matriz com os itens adicionados ficou: " + material_escolar;

    /// <h1 id="apagar_item_5">Apagar o item 5</h1>
    material_escolar.splice(5,1);
    document.getElementById("apagar_item_5").innerHTML = "A matriz sem o item 5 ficou: " + material_escolar;

    /// <h2 id="criar_matriz_2"></h2>
    const objetos_sala = ["mesa","cadeira"];
    document.getElementById("criar_matriz_2").innerHTML = "A nova matriz objetos_sala contem: " + objetos_sala;

    /// <h2 id="juntar_matriz"></h2>
    const material_com_objetos = material_escolar.concat(objetos_sala);
    document.getElementById("juntar_matriz").innerHTML = "A junção das matrizes 'material_escolar' e 'objetos_sala' ficou: " + material_com_objetos;

