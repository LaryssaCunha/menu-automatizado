# Menu - Lojinha
 ## Descrição Geral:
É um sistema de controle e registros financeiros para uma loja. Foi feito em linguagem Python, utilizando as bibliotecas sqlite3 para o banco de dados, numpy para os cálculos métricos e matplotlib para a visualização dos gráficos.

## ETAPAS DO PROJETO

1. Sobre o dataset:
      - Um dataset em csv com os seguintes dados:
            * Observações: Faturamento e despesas.
            * Variáveis: Ano e mês, entre 2018 a 2023.
      - A pasta 'script1' tem o dataset utilizado, e dois arquivos .py necessários para fazer a integração do arquivo CSV com o SQL.

2. Objetivo: Monitorar e atualizar registros integrado a um banco de dados SQLite com um menu automatizado de análises descritivas básicas. 
      O usuário pode:
      1. Adicionar um novo registro.
      2. Consultar os registros armazenados no banco de dados.
      3. Calcular o lucro filtrado por mês/ano.
      4. Visualizar os dados da receita geral (faturamentos, despesas e lucro) filtradas por ano em um único gráfico.
      5. Uma opção de saída.

3. Adicionei condições para caso o usuário não digite uma opção válida no menu.

### Considerações finais
Este sistema oferece uma interface baseada em texto para controle de registros financeiros, adequado aos pequenos negócios que desejam monitorar suas receitas e desepesas ao longo do tempo. A funcionalidade de geração de gráficos permite que o usuário visualize as tendências de faturamento, despesas e lucro com maior facilidade.

Essa documentação pode ser expandida conforme o código for sendo modificado ou aprimorado.
