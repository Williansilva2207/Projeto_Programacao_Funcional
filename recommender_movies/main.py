from data import catalogo, usuario
from recommender import pontuar_catalogo, recomendar

montar_resultado = lambda itens_pontuados, recomendacoes: {
    "itens_pontuados": itens_pontuados,
    "recomendacoes": recomendacoes,
}

executar_pipeline = lambda usuario_entrada, catalogo_entrada: (
    lambda itens_pontuados, recomendacoes: montar_resultado(
        itens_pontuados,
        recomendacoes,
    )
)(
    pontuar_catalogo(usuario_entrada, catalogo_entrada),
    recomendar(usuario_entrada, catalogo_entrada),
)

exibir_linha = lambda: print("-" * 60)

formatar_score = lambda item: (
    "" if item.get("score") is None else f" | score: {item['score']:.2f}"
)

exibir_item = lambda item: (
    print(f"{item['titulo']} ({item['tipo']})"),
    print(f"  Tags: {', '.join(item['tags'])}{formatar_score(item)}"),
)

exibir_lista = lambda titulo, itens: (
    print(titulo),
    exibir_linha(),
    list(
        map(
            exibir_item,
            itens,
        )
    ),
    print(),
)

resultado = executar_pipeline(usuario, catalogo)

print("SISTEMA DE RECOMENDACAO")
exibir_linha()
print(f"Usuario: {usuario['nome']}")
print(f"Interesses: {', '.join(usuario['interesses'])}")
print()

exibir_lista("CATALOGO ORIGINAL", catalogo)
exibir_lista("ITENS PONTUADOS", resultado["itens_pontuados"])
exibir_lista("RECOMENDACOES FINAIS", resultado["recomendacoes"])

