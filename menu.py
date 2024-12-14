import sqlite3

def menu():     #Menu automatizado
    while True:
        print("\n- - - MENU LOJINHA - - -")
        print("[ 1 ] Adicionar registro ")
        print("[ 2 ] Exibir registros")
        print("[ 3 ] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ano = int(input("Ano: "))
            mes = int(input("Mês: "))
            faturamento = float(input("Faturamento: "))
            despesas = float(input("Despesas: "))
            adicionar_registro(ano, mes, faturamento, despesas)
        elif opcao == "2":
            consulta_registros()
        elif opcao == "3":
            print("Encerrando o programa.")
            break

def adicionar_registro(ano, mes, faturamento, despesas):

#Conectar ao banco de dados
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

#Inserir os dados na tabela
    cursor.execute('''
                   INSERT INTO loja (ano, mes, faturamento, despesas)
                   VALUES (?, ?, ?, ?)
                ''', (ano, mes, faturamento, despesas))

#Salvar as mudanças e fechar a conexão
    conn.commit()
    conn.close()
    print("Registro adicionado com sucesso!")

#Função para exibir  todos os registros do banco de dados
def consulta_registros():

    #Conectar ao banco de dados
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

    #Buscar todos os registros
    cursor.execute("SELECT * FROM loja")
    registros = cursor.fetchall()

    #Exibir registros
    for registro in registros:
        print(registro)

    #Fechar conexão
    conn.close()

#Executar menu
menu()