#Ler o arquivo csv e registra-los no banco de dados.
import csv
import sqlite3

#Conexão com SQLite
conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

#Ler arquivo csv
with open('loja_faturamento_despesas.csv', 'r', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor) #Pular o cabeçalho
    for linha in leitor:
        cursor.execute('''
                       INSERT INTO loja (ano, mes, faturamento, despesas)
                       VALUES (?, ?, ?, ?)
                       ''',
                       (int(linha[0]), int(linha[1]), float(linha[2]), float(linha[3])))

#Atualizando e fechando a conexão
conn.commit()
cursor.close()
conn.close()