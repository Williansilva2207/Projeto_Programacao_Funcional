criar_conjunto = lambda valores: set(valores)

calcular_intersecao = lambda primeiro_conjunto, segundo_conjunto: (
    primeiro_conjunto.intersection(segundo_conjunto)
)

calcular_uniao = lambda primeiro_conjunto, segundo_conjunto: (
    primeiro_conjunto.union(segundo_conjunto)
)

calcular_indice_jaccard = lambda intersecao, uniao: (
    0 if len(uniao) == 0 else len(intersecao) / len(uniao)
)

similaridade_jaccard = lambda interesses, tags: calcular_indice_jaccard(
    calcular_intersecao(
        criar_conjunto(interesses),
        criar_conjunto(tags),
    ),
    calcular_uniao(
        criar_conjunto(interesses),
        criar_conjunto(tags),
    ),
)
