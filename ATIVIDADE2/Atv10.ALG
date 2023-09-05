Algoritmo "semnome"

Var
   //infantil A:5-7 | infantil B:8-10 | Juvenil A:11-13 | Juvenil B:14-17
   //Senior:18+
   idade: inteiro
Inicio
      escreva("Qual sua idade? ")
      leia(idade)
      SE idade < 8 ENTAO
         escreva("Categoria: infantil A!")
      SENAO
           SE idade < 11 ENTAO
              escreva("Categoria: infantil B!")
           SENAO
                SE idade < 14 ENTAO
                   escreva("Categoria: Juvenil A!")
                SENAO
                     SE idade < 18 ENTAO
                        escreva("Categoria: Juvenil B!")
                     SENAO
                          escreva("Categoria: Senior")
                     FIMSE
                FIMSE
           FIMSE
      FIMSE
Fimalgoritmo