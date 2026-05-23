from data import catalogo, usuario
from recommender import pontuar_catalogo, recomendar

def executar_pipeline(usuario_entrada, catalogo_entrada):

    itens_pontuados = pontuar_catalogo(usuario_entrada, catalogo_entrada)
    recomendacoes = recomendar(usuario_entrada, catalogo_entrada)

    return {
        "itens_pontuados": itens_pontuados,
        "recomendacoes": recomendacoes,
    }

def exibir_linha():
    print("-" * 60)

def exibir_item(item):
    score = item.get("score")
    score_texto = "" if score is None else f" | score: {score:.2f}"

    print(f"{item['titulo']} ({item['tipo']})")
    print(f"  Tags: {', '.join(item['tags'])}{score_texto}")

def exibir_lista(titulo, itens):
    print(titulo)
    exibir_linha()

    list(
        map(
            lambda item: exibir_item(item),
            itens,
        )
    )

    print()

resultado = executar_pipeline(usuario, catalogo)

print("SISTEMA DE RECOMENDACAO")
exibir_linha()
print(f"Usuario: {usuario['nome']}")
print(f"Interesses: {', '.join(usuario['interesses'])}")
print()

exibir_lista("CATALOGO ORIGINAL", catalogo)
exibir_lista("ITENS PONTUADOS", resultado["itens_pontuados"])
exibir_lista("RECOMENDACOES FINAIS", resultado["recomendacoes"])

