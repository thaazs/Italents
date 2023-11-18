programa {
  // Função principal do programa
  funcao inicio() {
    // Declaração de variáveis
    inteiro a , b , c
    inteiro auxiliar

   // Receber três números
  escreva("Digite o primeiro número: ")
  leia(a)
  escreva("Digite o segundo número: ")
  leia(b)
  escreva("Digite o terceiro número: ")
  leia(c)

  // Ordenar os números em ordem crescente
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
  escreva("Os números ordenados são: " + a, b, c)
  // Exibir os números ordenados

  }
}