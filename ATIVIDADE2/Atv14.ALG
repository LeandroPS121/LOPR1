Algoritmo "semnome"
//Fa�a um pseudoc�digo que leia o n�mero de litros vendidos e o
//tipo de combust�vel (codificado da seguinte forma: A-�lcool, G-gasolina),
//calcule e mostre o valor a ser pago pelo cliente sabendo-se que o pre�o do
//litro da gasolina � R$ 3,30 e o pre�o do litro do �lcool � R$ 2,90.

//alcool: ate 20L, desc de 3% por Litro
//      : acima de 20L, desc de 5% por Litro

//ate 20L, desc de 4%
//acima de 20L, desc de 6%

Var
   litrosVendidos: real
   tipoGasolina: caractere
   valorPagamento: real
Inicio
   escreva("Informe a quantidade de litro comprado: ")
   leia(litrosVendidos)
   escreva("Informe o tipo de gasolina(A-Alcool ; G-Gasolina):")
   leia(tipoGasolina)
   SE tipoGasolina = "G" ENTAO
      SE litrosVendidos <= 20 ENTAO
         valorPagamento <- 3.3 * litrosVendidos - 0.04 * litrosVendidos
         escreva("Total a pagar: ",valorPagamento)
      SENAO
           valorPagamento <- 3.3 * litrosVendidos - 0.06 * litrosVendidos
           escreva("Total a pagar: ",valorPagamento)
      FIMSE
   SENAO
      SE litrosVendidos <= 20 ENTAO
         valorPagamento <- 2.9 * litrosVendidos - 0.03 * litrosVendidos
         escreva("Total a pagar: ",valorPagamento)
      SENAO
           valorPagamento <- 2.9 * litrosVendidos - 0.05 * litrosVendidos
           escreva("Total a pagar: ",valorPagamento)
      FIMSE
   FIMSE

Fimalgoritmo