programa {
  // Fun��o principal do programa
  funcao inicio() {
    // Declara��o de vari�veis
    inteiro a , b , c
    inteiro auxiliar

   // Receber tr�s n�meros
  escreva("Digite o primeiro n�mero: ")
  leia(a)
  escreva("Digite o segundo n�mero: ")
  leia(b)
  escreva("Digite o terceiro n�mero: ")
  leia(c)

  // Ordenar os n�meros em ordem crescente
  se (a > b){
   auxiliar = a
   a = b
   b = auxiliar
  }

   se (c < b){
    auxiliar = b
    b = c
    c = auxiliar
   }

    se (b < a){
      auxiliar = a
      a = b
      b = auxiliar
    }
  escreva("Os n�meros ordenados s�o: " + a, b, c)
  // Exibir os n�meros ordenados

  }
}