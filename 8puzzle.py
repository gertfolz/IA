import solucao as solucao

if __name__ == '__main__':
    nodoRaiz = solucao.Nodo("_23541687", None, None, 0)
    nodos = []
    nodos = solucao.expande(nodoRaiz)

    for i in range(len(nodos)):
        print(nodos[i].estado)
        print(nodos[i].acao)
        print(nodos[i].custo)
        

