Algoritmo "semnome"
//Faça um pseudocódigo que leia o número de litros vendidos e o
//tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
//calcule e mostre o valor a ser pago pelo cliente sabendo-se que o preço do
//litro da gasolina é R$ 3,30 e o preço do litro do álcool é R$ 2,90.

//alcool: ate 20L, desc de 3% por Litro
//      : acima de 20L, desc de 5% por Litro

//ate 20L, desc de 4%
//acima de 20L, desc de 6%

Var
   litrosVendidos: real
   tipoGasolina: logico
   valorPagamento
Inicio
      escreva("Informe a quantidade de litro comprado: ")
      leia(litrosVendidos)
      escreva("Informe o tipo de gasolina(A-Alcool ; G-Gasolina):")
      leia(tipoGasolina)
      SE tipoGasolina = "A" ENTAO
         SE litrosVendidos <= 20 ENTAO
            valorPagamento <- 2.9 * litrosVendidos
            escreva("Total a pagar: ",valorPagamento)
Fimalgoritmo