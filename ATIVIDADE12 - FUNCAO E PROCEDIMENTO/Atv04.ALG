Algoritmo "semnome"

Var

   ehPrimo: logico
   numero: inteiro
Inicio
   escreval("Digite o intervalo entre 2 e 100:")
   leia(numero)
   escreval
   ehPrimo <- VERDADEIRO
FUNCAO verificaPrimo(): inteiro
VAR
   i: inteiro
INICIO
   enquanto numero >= 2 faca
      para i de 2 ate numero - 1 faca
         SE numero % i = 0 ENTAO
            ehPrimo <- FALSO
         FIMSE
      fimpara
      SE (ehPrimo = VERDADEIRO) e (numero <> 2) ENTAO
         escreval(numero)
      FIMSE
      numero <- numero - 1
      ehPrimo <- VERDADEIRO
   fimenquanto
   retorne 2
FIMFUNCAO
escreval(verificaPrimo())


Fimalgoritmo

