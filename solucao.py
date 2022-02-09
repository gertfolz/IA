class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado:str = estado
        self.pai:Nodo = pai
        self.acao:str = acao
        self.custo:int = custo

def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

    pos = estado.find('_')                  # Acha a posição do espaço em branco    
    listaSucessores = []

    if pos != (0 and 3 and 6):              # Mexe o espaço branco pra esquerda
        estadoAux = list(estado)            # Transforma a string em uma lista pois strings são imutáveis
        estadoAux[pos], estadoAux[pos - 1] =  estadoAux[pos - 1], estadoAux[pos]    # Troca os caracteres de posição
        listaSucessores.append(("esquerda", ''.join(estadoAux)))                    # Junta a tupla da ação e o novo estado no final da lista de sucessores
    
    if pos != (2 and 5 and 8):              # Mexe o espaço branco pra direita
        estadoAux = list(estado)           
        estadoAux[pos], estadoAux[pos + 1] =  estadoAux[pos + 1], estadoAux[pos]
        listaSucessores.append(("direita", ''.join(estadoAux)))

    if pos != (0 and 1 and 2):              # Mexe o espaço branco pra cima
        estadoAux = list(estado)           
        estadoAux[pos], estadoAux[pos - 3] =  estadoAux[pos - 3], estadoAux[pos]
        listaSucessores.append(("acima", ''.join(estadoAux)))

    if pos != (6 and 7 and 8):              # Mexe o espaço branco pra baixo
        estadoAux = list(estado)            
        estadoAux[pos], estadoAux[pos + 3] =  estadoAux[pos + 3], estadoAux[pos]
        listaSucessores.append(("abaixo", ''.join(estadoAux)))

    print(listaSucessores)
    return listaSucessores


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

    listaSucessores = []
    novosNodos = []
    listaSucessores = sucessor(nodo.estado)

    for i in range(len(listaSucessores)):
        tupla = listaSucessores[i]
        novoNodo = Nodo(tupla[1], nodo, tupla[0], nodo.custo + 1)
        novosNodos.append(novoNodo)
    
    return novosNodos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
