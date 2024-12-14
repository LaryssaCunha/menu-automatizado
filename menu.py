import sqlite3
import numpy as np
import matplotlib.pyplot as plt

def menu():     #Menu automatizado
    while True:
        print("\n- - - MENU LOJINHA - - -")
        print("[ 1 ] Adicionar registro ")
        print("[ 2 ] Exibir registros")
        print("[ 3 ] Exibir lucro por mês/ano")
        print("[ 4 ] Gerar gráfico da receita por ano")
        print("[ 5 ] Sair")
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
            ano = int(input("Digite o ano: "))
            mes = int(input("Digite o mês: "))
            lucros = calcular_metricas(ano, mes)
            if lucros is not None:
                print(f"Os lucros para o {mes:02}-{ano} é de {lucros}")

        elif opcao == "4":
            ano = int(input("Ano: "))
            gerar_grafico(ano)

        elif opcao == "5":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida! Tente novamente. ")

#Função para adicionar novos registros
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

#Função para calcular as métricas do lucro filtradas por mês/ano
def calcular_metricas(ano, mes):
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

#Selecionar os registros filtrados
    cursor.execute('''
        SELECT faturamento, despesas
        FROM loja 
        WHERE ano = ? AND mes = ?
    ''', (ano, mes))
    registros = cursor.fetchall()
    conn.close()

    if not registros:
        print("Nenhum registro encontrado para o ano e o mês especificados.")
        return None, None, None, None
    
#Calcular o lucro para os registros selecionados
    lucros = [faturamento - despesas for faturamento, despesas in registros]
    return lucros

def gerar_grafico(ano):
    conn = sqlite3.connect("loja.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT mes, faturamento, despesas
        FROM loja
        WHERE ano = ?
        ORDER BY mes
    ''', (ano,))
    registros = cursor.fetchall()
    conn.close()

    if not registros:
        print("Nenhum registro encontrado para o ano especificado.")
        return
    
    meses = [registro[0] for registro in registros]
    faturamentos = [registro[1] for registro in registros]
    despesas = [registro[2] for registro in registros]
    lucros = [ f - d for f, d in zip(faturamentos, despesas)]

#Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(meses, faturamentos, label="Faturamento", marker="o", color="blue")
    plt.plot(meses, despesas, label="Despesas", marker="o", color="red")
    plt.plot(meses, lucros, label="Lucro", marker="o", color="green")

    plt.title(f"Receita geral do ano de {ano}")
    plt.xlabel("Meses")
    plt.ylabel("Valores")
    plt.legend()
    plt.grid(True)
    plt.xticks(range(1, 13)) #Exibir todos os meses no eixo x
    plt.show()

#Executar menu
menu()