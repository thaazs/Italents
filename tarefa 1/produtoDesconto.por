programa {
  // Fun��o principal do programa
  funcao inicio() {
    // Declara��o de vari�veis
    real valorProduto
    real desconto
    real valorFinal

    // Receber o valor do produto do usu�rio
    escreva("Digite o valor do produto: ")
    leia(valorProduto)

    // Calcular o desconto (10% do valor do produto)
    desconto = valorProduto * 0.10

    // Calcular o valor final com desconto
    valorFinal = valorProduto - desconto

    // Exibir o resultado
    escreva("O valor final com desconto �: ", valorFinal)
  }
}
