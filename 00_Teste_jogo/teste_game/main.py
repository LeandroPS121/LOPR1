import os
import random

inicio = True
tutorial = True
jogo_ganho = False

hp_jogador_maximo  = 0
str_jogador = 0
mp_jogador  = 0
id_estilo = 0
skill_list = ["DISPAROS RÁPIDOS","TIRO CONCENTRADO [MP-3]","DISPAROS DE GRANADA [HP-10]",
              "CORTE VERTICAL","CORTE DUPLO","CORTE GIRATÓRIO",
              "ESCUDADA","CRITICAL","ARREMESSA ESPINHOS [STR-5]"]

while inicio == True:
    os.system('cls')
    print("escolha um estilo de jogo: ")
    print("ataque     [1]")
    print("equilíbrio [2]")
    print("defensivo  [3]")
    escolha_estilo = input("--> ")
    os.system('cls')

    match escolha_estilo:
        case "1":
            print("estilo: ATAQUE")
            print()
            print("atributos:")
            print("HP   [20] ")
            print("STR  [50]*")
            print("MP   [10] ")

            hp_jogador_maximo  = 20
            str_jogador  = 50
            mp_jogador   = 10
            arma_jogador = "2x Metralhadoras! (muito poder e em dobro.. )"

            id_estilo = 1
            sk_a = 0
            sk_b = 1
            sk_c = 2

        case "2":
            print("estilo: EQUILÍBRIO")
            print()
            print("atributos: ")
            print("HP   [35]* ")
            print("STR  [35]* ")
            print("MP   [10]  ")

            hp_jogador_maximo  = 35
            str_jogador  = 35
            mp_jogador   = 10
            arma_jogador = "Espada Longa! (simples demais.. espera aí.. Guts?)"

            id_estilo = 2
            sk_a = 3
            sk_b = 4
            sk_c = 5
        case "3":
            print("estilo: DEFENSIVO")
            print()
            print("atributos:")
            print("HP   [50]*")
            print("STR  [20] ")
            print("MP   [10] ")
            
            hp_jogador_maximo  = 50
            str_jogador  = 20
            mp_jogador   = 10
            arma_jogador = "Escudo com Espinhos! (o Sonic sentiria inveja..)"

            id_estilo = 3
            sk_a = 6
            sk_b = 7
            sk_c = 8
        case _:
            os.system('cls')
            print("OPCÃO INVÁLIDA")
            input("--> ")
    if escolha_estilo == "1" or escolha_estilo == "2" or escolha_estilo == "3":
        print()
        print("deseja escolher este estilo? sim[1]/não[2]")
        confirma_estilo = input("--> ")

        match confirma_estilo:
            case "1":
                inicio = False
            case "2":
                pass
            case _:
                os.system('cls')
                print("OPÇÃO INVÁLIDA")
                input("--> ")

os.system('cls')
print("Antes de começar a jogar, você aprenderá como funciona as mecânicas do jogo.")
input("--> ")

while tutorial == True:
    tutorial_valido = False

    os.system('cls')
    print("Esta será a tela de combate:")
    print("-Inimigo- [5|70]    ")
    print("                    ")
    print("                    ")
    print("-Jogador- [ATAQUE-1] [ESPIRITO-2]   ")
    print("          [ITEM-3  ] [STATUS-4  ]   ")
    input("--> ")
    os.system('cls')
    print("HP:  HEALTH POINTS -> pontos de vida, se chegar a 0 você perde!")
    print("STR: STRENGTH  -> pontos de força, acabe com os inimigos!")
    print("DEF: DEFENSE  -> pontos de defesa, torne-se intankável!")
    print("MP:  MAGIC POINTS  -> pontos mágicos, igual imposto, você paga, mas nesse caso tem algo bom em troca!")
    input("--> ")
    os.system('cls')
    print("-Inimigo- [A|B] \n")
    print("A: ATAQUE do inimigo")
    print("B: HP do inimigo")
    input("--> ")
    os.system('cls')
    print("-Jogador- [ATAQUE-1] [ESPIRITO-2]   ")
    print("          [ITEM-3  ] [STATUS-4  ]   ")
    print("ATAQUE: escolha um tipo de ataque NORMAL/ESPECIAL")
    input("--> ")
    os.system('cls')
    print("ATAQUES normais causam um dano baixo sem custo")
    print("ATAQUES especiais causam um dano moderado usando MP")
    input("--> ")
    os.system('cls')
    print("ESPIRITO: reduz o dano sofrido neste turno em 1/4 &")
    print("          aumente o dano causado no próximo turno")
    input("--> ")
    os.system('cls')
    print("ITEM: abre a mochila de itens")
    input("--> ")
    os.system('cls')
    print("STATUS: verifica status e atributos do jogador")
    input("--> ")

    while tutorial_valido == False:
        os.system('cls')
        print("Este foi o tutorial, deseja ver novamente? sim[1]/não[2]")
        escolha_tutorial = input("--> ")

        if escolha_tutorial == "1":
            tutorial_valido = True
        elif escolha_tutorial == "2":
            tutorial_valido = True
            tutorial = False
        else:
            os.system('cls')
            print("OPÇÃO INVÁLIDA")
            input("--> ")

os.system('cls')
print("Iniciar Jogo")
input("--> ")
inimigos = ["Palusk","João","Fernanda","Eros","Brunno","Alann"]

hp_jogador = hp_jogador_maximo
while jogo_ganho == False:
    os.system('cls')
    defense = 1
    i = random.randint(0,5)
    hp_inimigo = random.randint(75,100)
    str_inimigo = random.randint(5,8)

    print(f"inimigo encontrado: {inimigos[i]}")
    print("-iniciar batalha-")
    input("--> ")
    os.system('cls')

    partida_finalizada = False
    cancelar_acao = True
    while partida_finalizada == False:
        while cancelar_acao == True:
            cancelar_acao = True
            esp = 1
            print(f"-{inimigos[i]}- [{str_inimigo}|{hp_inimigo}]")
            print("                    ")
            print("                    ")
            print("-Jogador- [ATAQUE-1] [ESPIRITO-2]   ")
            print("          [ITEM-3  ] [STATUS-4  ]   ")
            acao = input("-->")

            os.system('cls')
            match acao:
                case "1":
                    cancelar_acao = False
                    print("Escolha um ATAQUE:\n")
                    print(f"{sk_a}[1] \n{sk_b}[2] \n{sk_c}[3]")
                    ataque_escolhido = input() #continuar
                case "2":
                    cancelar_acao = False
                    esp = 1.25 #dividir
                case "3":
                    print("MOCHILA: \n")
                    print("SUCO DE LIMÃO   --40% + HP--   [1]")
                    print("SUCO DE CIMENTO --100% + DEF-- [2]")
                    item_escolhido = input("--> ")
                    if item_escolhido == 1:
                        cancelar_acao = False
                        hp_jogador += (hp_jogador_maximo // 2.2)
                        if hp_jogador > hp_jogador_maximo:
                            hp_jogador = hp_jogador_maximo
                    elif item_escolhido == 2:
                        cancelar_acao = False
                        defense += 1
                    else:
                        cancelar_acao = True
                        print("OPÇÃO INVÁLIDA")
                        input("-->")
                case "4":
                    cancelar_acao = True
                    print("STATUS do jogador: \n")
                    print(f"HP: {hp_jogador}/{hp_jogador_maximo}\nSTR: {str_jogador}\nMP: {mp_jogador} \n\nArma: {arma_jogador}")
                    input("--> ")