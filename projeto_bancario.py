'''
        Operações
  - Depósito:
  Depositar valores positivos
  Devem ser armazenadas em uma unica variavel para utilizar a função extrato

  - Saque
  É possível realizar 3 saques, com limite de 500 reais
  Todo saque tem que ser armazenado em um variavel para o extrato


  
  
Extrato:

Deve listar todas as operações
Deve exibir o saldo
 '''


menu = """
===============MENU===============

            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair

===================================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []

while True:

    opcao = input (menu)

    if opcao == "d":
        deposito = float(input("Informe um valor de depósito:  "))
        if deposito > 0:
                saldo = deposito + saldo
                extrato.append(f"Depósito: + R${deposito}")                
                print(f"O valor do depósito é de {deposito}")
                print(f"Seu saldo é de R${saldo} ")
                


    elif opcao == "s":
        sacar = float(input("Digite um valor que deseja sacar"))
        
        if sacar <= saldo and numero_saques <= LIMITE_SAQUES and saldo > 0 and sacar <= 500:
             numero_saques = numero_saques + 1
             saldo = saldo - sacar
             extrato.append(f"Saque: - R${sacar}")
                          
             print(f"Você só pode efetuar três saques e você ja sacou {numero_saques}")
             print(f"Você sacou um valor de R${sacar} e seu saldo atual é de R${saldo} ")
        else:
             print("Operação invalida, Verifique seu saldo ou limite de saque diario")
        
        
    elif opcao == "e":
        print("Extrato")
        
        for operacao in extrato:
             print(operacao)
        
        print(saldo)



    elif opcao == "q":
        break

    else:
        print("Digite uma opção válida")
    