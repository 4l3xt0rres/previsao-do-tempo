# Previsão do Tempo com Python, Selenium e Pandas

## Metodologia 5W1H

### What (O quê?)
Um programa em Python que acessa o site Time and Date e coleta automaticamente a previsão do tempo para até 7 dias de uma cidade brasileira escolhida pelo usuário.  
Os dados coletados (dia, temperaturas máxima e mínima e condição climática) são exportados para um arquivo CSV.

### Why (Por quê?)
- Automatizar a busca de informações de previsão do tempo.  
- Demonstrar o uso prático de web scraping com Selenium.  
- Aplicar bibliotecas do Python como Pandas para organizar e salvar dados.  
- Desenvolver um projeto multiplataforma (Windows e Linux).  

### Who (Quem?)
- Desenvolvedor: Alunos de Ciência da Computação.  
- Usuário final: Qualquer pessoa que queira consultar previsões meteorológicas de forma automatizada.  
- Tecnologias usadas:  
  - Python 3.13+  
  - Selenium  
  - Pandas  
  - WebDriver Manager  

### Where (Onde?)
- Funciona em Windows e Linux (não precisa baixar manualmente o ChromeDriver, o código faz isso automaticamente).  
- Site usado: Time and Date (https://www.timeanddate.com/weather/).  

### When (Quando?)
- Pode ser usado a qualquer momento para consultar previsões de até 7 dias futuros.  
- O CSV gerado pode ser utilizado em relatórios, trabalhos acadêmicos ou no dia a dia.  

### How (Como?)
1. Instalar as dependências:
   pip install selenium pandas webdriver-manager

2. Executar o programa:
   python main.py

3. Digitar o nome da cidade:  
   - Exemplo: sao paulo  
   - Exemplo: rio de janeiro  

4. O resultado será salvo no arquivo:
   previsao.csv
