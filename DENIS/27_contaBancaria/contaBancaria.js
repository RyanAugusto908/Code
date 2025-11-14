// 1 Ckasse reoresentando uma conta bancária
class ContaBancaria{
    // Declaração da classe 'ContaBancaria'.
    // Atributo privado: só pode ser acessado dentro da classe
    #saldo = 0;
    // Declara o atributo '#saldo'. O '#' torna ele privado, impedindo acesso/modificação externa. Inicializa com 0.

    // Método para depositar um valor
    depositar(valor){
        // Define um método público 'depositar' que recebe 'valor' como argumento
        if(valor>0){
        // Verifica se o valor a ser depositado é positivo.
        this.#saldo += valor;    
        } else{
        // Se a condição (valor > 0) for falsa.
            console.log("Valor in´valido para depósito!");
        }
    }

    verSaldo(){
        console.log(`Saldo atual: R$ ${this.#saldo}`);
    }
}

// Usando a classe
const conta =  new ContaBancaria();
conta.depositar(1000);
// chama o método 'verSaldo', que acesa e exibe o saldo(1000).
// conta.#saldo = 5000; Erro - não pode acessar atributo privado.
// Esta linha causaria um erro de sitaxe, pois o '#' impede acesso direto de fora da classe.

// 2 Classe que representa uma impressora
class impressora{
    imprimir(documento){
        this.#iniciarImpressora();
        this.#carregarTinta();
        console.log(`Imprimindo: ${documento}`);
        this.#finalizarImpressao();
        // chama o método privado '#finalizarImpressao' (detalhe de implementação).
    }

    #iniciarImpressora(){
        console.log("Inicializando impressora...");
    }

    #carregarTinta(){
        console.log("Carregando tinta...");
    }
    #finalizarImpressao(){
        console.log("Impressão concluída.");
    }
}

const impressora = new Impressora();
impressora.imprimir("Relatório.pdf");

class Pedido{
    constructor(cliente, itens) {
        this.cliente = cliente;
        this.itens = itens;
        // Define a propriedade 'itens' no objeto (público).
    }

    // Método principal que o usuário chama
    finalizarPedido(){
        const total = this.#calcularTotal();
        if(this.#validarItens()){
            console.log(`Pedido de ${this.cliente} finalizado. Total: R$ ${total}`);
            this.#enviarConfirmacao();
            // Chama o método privado '#enviarConfirmação'.
        }
    }

    #validarItens(){
        return this.itens.lenght > 0;
    }

    #calcularTotal(){
        return this.itens.reduce((soma,item) => soma + item.preco,0);
    }

    #enviarConfirmacao(){
        console.log("Email de confirmação enviado!");
    }
}

const pedido = new Pedido("Carlos", [
    {nome: "Mouse", preco: 80},
    {nome: "Teclado", preco: 150}
]);
pedido.finalizarPedido();
// Chama o métoo público 'finalizarPedido', que executa os passos internos (privados) de validação, cálculo e envio.