from similarity import similaridade_jaccard

def pontuar_item(usuario, item):
    return {
        **item,
        "score": similaridade_jaccard(usuario["interesses"], item["tags"]),
    }

def pontuar_catalogo(usuario, catalogo):
    return list(
        map(
            lambda item: pontuar_item(usuario, item),
            catalogo,
        )
    )

def filtrar_relevantes(itens_pontuados):
   
    return list(
        filter(
            lambda item: item["score"] > 0,
            itens_pontuados,
        )
    )

def ordenar_por_relevancia(itens):
    return sorted(
        itens,
        key=lambda item: (-item["score"], item["titulo"]),
    )

def recomendar(usuario, catalogo):
    return ordenar_por_relevancia(
        filtrar_relevantes(
            pontuar_catalogo(usuario, catalogo)
        )
    )
