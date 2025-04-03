""" PROJETO CALCULADORA """
import math

# Variaveis
avalia = str
checa = str
cont=0
list_soma =[]
list_sub=[]
list_mut=[]
list_div=[]

# Imprime o Titulo da aplicação.
print("######### CALCULADORA ###########")

# Bloco de seleção de operações.
while checa != "Fim":
    print("Selecione a operação desejada.")
    selecao = str(input(" + , - , X , / "))

    #Bloco de adição: recebe os dados, soma, imprime e adiciona a lista
    if selecao == "+":
        print("Função de adição selecionada.")
        print("Introduza as parcelas para a soma.")
        while avalia != "Retornar":
            parcela = float(input("Digite a primeira parcela: "))
            parcela2 = float(input("Digite a segunda parcela: "))
            soma = parcela + parcela2
            print(f"SOMA = {soma}")
            list_soma.append(soma)
            cont=cont+1
            avalia = input("Calcular novamente? Caso sim precione o Enter, ou Retornar para retornar ao menu de seleção.")
        print("Lista de somas realizadas: ")
        for i in range(0, cont):
            print(f"{list_soma[i]}",end="  ")
            print("    ")

    #Bloco de Subtração: recebe os dados, subritrae, imprime e adiciona a lista
    elif selecao == "-":
        print("Função subtração selecionada.")
        print("Adicione o subtrativo e o aditivo para a subtração.")
        while avalia != "Retornar":
            subtrativo = float(input("Digite o subtrativo: "))
            aditivo = float(input("Digite o aditivo:"))
            subtracao = subtrativo - aditivo
            print(f"Subtração = {subtracao}")
            list_sub.append(subtracao)
            cont = cont + 1
            avalia = input("Calcular novamente? Caso sim precione o Enter, ou Retornar para retornar ao menu de seleção.")
        print("Lista de subtrações realizadas: ")
        for i in range(0,cont):
                print(f"{list_sub[i]}",end="  ")
                print("   ")

    #Bloco de Multiplicação: recebe os dados, multiplica, imprime e adiciona a lista
    elif selecao == "*":
        print("Função Multiplicação selecionada.")
        print("Adicione os fatores para a multiplicação.")
        while avalia != "Retornar":
            fator = float(input("Diigite o primeiro fator: "))
            fator2 = float(input("Digite o segundo fator: "))
            produto = fator * fator2
            print(f"Produto = {produto}")
            list_mut.append(produto)
            cont = cont + 1
            avalia = input("Calcular novamente? Caso sim precione o Enter, ou Retornar para retornar ao menu de seleção.")
        print("Lista de mutiplicações realizadas: ")
        for i in range(0,cont):
            print(f"{list_mut[i]}",end="   ")
            print("  ")

    #Bloco de Divisão: recebe os dados, divide, imprime e adiciona a lista
    elif selecao == "/":
        print("Função Divisão selecionada.")
        print("Adicione o dividendo e divisor para a divisão.")
        while avalia != "Retornar":
            dividendo = float(input("Digite o dividendo: "))
            divisor = float(input("Digite o divisor"))
            quociente = dividendo / divisor
            print(f"Quociente = {quociente}")
            list_div.append(quociente)
            cont = cont + 1
            avalia = input("Calcular novamente? Caso sim precione o Enter, ou Retornar para retornar ao menu de seleção.")
        for i in range(0,cont):
            print(f"{list_div[i]}",end="  ")
            print("   ")

    #Reset de dados.
    cont =0
    avalia = "   "
    checa=input("Deseja continuar?Precione Enter, caso não digite Fim")
