# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.
from typing import Dict, Any

livros: Dict[str, Any] = {
    "titulo": "O simbolo Perdido", 
    "autor": "Dan Brown", 
    "ano": 2009
}
for chave, valor in livros.items():
    print(f"{chave}: {valor}")