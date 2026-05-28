from similarity import similaridade_jaccard

calcular_score = lambda usuario, item: similaridade_jaccard(
    usuario["interesses"],
    item["tags"],
)

pontuar_item = lambda usuario, item: {
    **item,
    "score": calcular_score(usuario, item),
}

pontuar_catalogo = lambda usuario, catalogo: list(
    map(
        lambda item: pontuar_item(usuario, item),
        catalogo,
    )
)

item_tem_relevancia = lambda item: item["score"] > 0

chave_relevancia = lambda item: (-item["score"], item["titulo"])

filtrar_relevantes = lambda itens_pontuados: list(
    filter(
        item_tem_relevancia,
        itens_pontuados,
    )
)

ordenar_por_relevancia = lambda itens: sorted(
    itens,
    key=chave_relevancia,
)

recomendar = lambda usuario, catalogo: ordenar_por_relevancia(
    filtrar_relevantes(
        pontuar_catalogo(usuario, catalogo)
    )
)
