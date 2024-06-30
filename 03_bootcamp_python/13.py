# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API

while pagina_atual < paginas_totais:
    print(f"Acessando página {pagina_atual} de {paginas_totais}")
    ### código de dentro da página 
    pagina_atual += 1
print(f"Todas as {paginas_totais} foram processadas")