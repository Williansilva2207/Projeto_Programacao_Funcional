def similaridade_jaccard(interesses, tags):

    conjunto_interesses = set(interesses)
    conjunto_tags = set(tags)
    intersecao = conjunto_interesses.intersection(conjunto_tags)
    uniao = conjunto_interesses.union(conjunto_tags)

    return 0 if len(uniao) == 0 else len(intersecao) / len(uniao)