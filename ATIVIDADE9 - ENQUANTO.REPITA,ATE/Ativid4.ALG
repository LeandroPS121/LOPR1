Algoritmo "semnome"

Var
   numero,numero2: real
   opcao: caractere
Inicio
   repita
      escreval("[1] somar")
      escreval("[2] subtrair")
      escreval("[3] multiplicar")
      escreval("[4] dividir")
      escreval("[5] sair")
      leia(opcao)
      se opcao <> "5" entao
         escreval("Digite um numero")
         leia(numero)
         escreval("Digite outro numero")
         leia(numero2)
         escolha opcao
         caso "1"
            escreval(numero," +",numero2," =",numero+numero2)
         caso "2"
            escreval(numero," -",numero2," =",numero-numero2)
         caso "3"
            escreval(numero," x",numero2," =",numero*numero2)
         caso "4"
            escreval(numero," /",numero2," =",numero/numero2)
         outrocaso
            escreval("Invalido")
         fimescolha
      fimse
      escreval("FIM")
   ate opcao = "5"
Fimalgoritmo