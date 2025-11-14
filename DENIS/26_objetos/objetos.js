// Exemplo: Criando um objeto simples chamado "carro"

// Cria um objeto literal chamado "carro"
const carro = {
    marca: "Toyota",
    modelo: "Corolla",
    ano: 2020,
    ligar: function(){
        console.log("O carro está ligado!");
    },

    mostrarInfo: function(){
        console.log(`${this.marca} ${this.modelo} - Ano: ${this.ano}`);
    }
};

carro.ligar();
carro.mostrarInfo();

function Pessoa(nome, idade){
    this.nome = nome;
    this.idade = idade;
    this.apresentar = function(){
        console.log(`Olá meu nome é ${this.nome} e tenho ${this.idade} anos.`);
    };
}

const pessoal1 = new Pessoa("Denis", 44);
const pessoal2 = new Pessoa("Maria", 25);

pessoal1.apresentar();
pessoal2.apresentar();

const aluno = {
    nome: "João",
    idade: 17,
    endereco: {
        rua: "Rua das Flores",
        numero: 123,
        cidade: "São Paulo"
    },

    mostrarEndereco: function(){
        console.log(`${this.nome} mora na ${this.endereco.rua}, nº ${this.endereco.numero}`);
    }
};

aluno.mostrarEndereco();


const produtos = [
    {nome: "Teclado", preco: 150},
    {nome: "Mouse", preco: 100},
    {nome: "Monitor", preco: 800}
];

produtos.forEach(produto =>{
    console.log(`${produto.nome} custa R$${produto.preco}`);
});

const total = produtos.reduce((soma, produto) => soma + produto.preco, 0);
console.log("Total: R$" + total);