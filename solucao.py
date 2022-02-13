from distutils import dist
import math
from os import remove


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
        self.estado: str = estado
        self.pai: Nodo = pai
        self.acao: str = acao
        self.custo: int = custo


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo

    # Acha a posição do espaço em branco
    pos = estado.find('_')
    listaSucessores = []
    if pos not in [0, 3, 6]:              # Mexe o espaço branco pra esquerda
        # Transforma a string em uma lista pois strings são imutáveis
        estadoAux = list(estado)
        estadoAux[pos], estadoAux[pos - 1] = estadoAux[pos -
                                                       1], estadoAux[pos]    # Troca os caracteres de posição
        # Junta a tupla da ação e o novo estado no final da lista de sucessores
        listaSucessores.append(("esquerda", ''.join(estadoAux)))

    if pos not in [2, 5, 8]:              # Mexe o espaço branco pra direita
        estadoAux = list(estado)
        estadoAux[pos], estadoAux[pos + 1] = estadoAux[pos + 1], estadoAux[pos]
        listaSucessores.append(("direita", ''.join(estadoAux)))

    if pos not in [0, 1, 2]:              # Mexe o espaço branco pra cima
        estadoAux = list(estado)
        estadoAux[pos], estadoAux[pos - 3] = estadoAux[pos - 3], estadoAux[pos]
        listaSucessores.append(("acima", ''.join(estadoAux)))

    if pos not in [6, 7, 8]:              # Mexe o espaço branco pra baixo
        estadoAux = list(estado)
        estadoAux[pos], estadoAux[pos + 3] = estadoAux[pos + 3], estadoAux[pos]
        listaSucessores.append(("abaixo", ''.join(estadoAux)))

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
    # Armazena os sucessores calculados para o estado numa nova lista
    listaSucessores = sucessor(nodo.estado)

    # Itera por toda lista de sucessores
    for i in range(len(listaSucessores)):
        # Armazena a tupla (acao, estado)
        tupla = listaSucessores[i]
        # Cria um novo nodo para cada sucessor do nodo pai
        novoNodo = Nodo(tupla[1], nodo, tupla[0], nodo.custo + 1)
        # Salva o novo nodo criado em uma lista que será retornada
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

    # Cria um novo nodo para conseguir rastrear o caminho através do atributo 'pai'
    nodoRaiz = Nodo(estado, None, None, 0)
    # Inicializa a fronteira com o nodo raíz
    listaFronteira = [nodoRaiz]
    setExplorados = set()
    # Enquanto a lista da fronteira não for vazia ou o set de explorados for menor que o número máximo dos estados do jogo (9!/2)
    while listaFronteira and len(setExplorados) <= 181440:
        # Como é busca por largura, a lista se comporta como uma fila FIFO
        novoNodo = listaFronteira.pop(0)
        # Se o novo estado é o objetivo, chama a função que calcula o caminho do nodo até o nodo pai
        if (novoNodo.estado == "12345678_"):
            return achaCaminho(novoNodo)
        # Se o estado do novo nodo esta na lista de explorados, nao expande, evitando que entre em um loop
        if novoNodo.estado not in setExplorados:
            # Adiciona novos nodos à fronteira
            listaFronteira.extend(expande(novoNodo))
            # Atualiza o set de estados já explorados
            setExplorados.add(novoNodo.estado)

    return None


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
    nodoRaiz = Nodo(estado, None, None, 0)
    listaFronteira = [nodoRaiz]
    setExplorados = set()

    while listaFronteira and len(setExplorados) <= 181440:
        # Única diferença à função de bfs é que aqui a lista é implementada como uma pilha (removendo sempre o último elemento da lista)
        novoNodo = listaFronteira.pop(len(listaFronteira)-1)
        if (novoNodo.estado == "12345678_"):
            return achaCaminho(novoNodo)
        if novoNodo.estado not in setExplorados:
            listaFronteira.extend(expande(novoNodo))
            setExplorados.add(novoNodo.estado)

    return None


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
    explorados = set()                              # Cria set de explorados e min-heap de fronteiras
    fronteira = [Nodo(estado, None, None, calcula_heuristica_hamming(estado))]

    while True:
        if len(fronteira) == 0:                     # Se o heap de fronteiras estiver vazio, o puzzle não tem solução
            return None

        if fronteira[0].estado == "12345678_":      # Se o primeiro elemento do heap for o estado final, a solução ótima foi encontrada
            movimentos = []
            elemento = fronteira[0]

            while elemento.pai is not None:
                movimentos.insert(0, elemento.acao) # Insere movimentos efetuados em uma lista para retornar
                elemento = elemento.pai

            return movimentos

        novosEstados = expande(fronteira[0])        # Expande o primeiro elemento do heap

        for item in novosEstados:                   # Para cada novo estado encontrado, inseri-lo no heap se já não tiver sido explorado posteriormente
            if item.estado not in explorados:
                novoItem = Nodo(item.estado, item.pai, item.acao, item.custo + calcula_heuristica_hamming(item.estado))
                insere_min_heap(novoItem, fronteira)

        explorados.add(fronteira[0].estado)                                     # Adicionar primeiro elemento do heap na lista de explorados, e removê-lo do heap
        remove_primeiro_min_heap(fronteira)


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
    # Cria set de explorados e min-heap de fronteiras
    explorados = set()
    fronteira = [
        Nodo(estado, None, None, calcula_heuristica_manhattan(estado))]

    while True:
        # Se o heap de fronteiras estiver vazio, o puzzle não tem solução
        if len(fronteira) == 0:
            return None

        # Se o primeiro elemento do heap for o estado final, a solução ótima foi encontrada
        if fronteira[0].estado == "12345678_":
            movimentos = []
            elemento = fronteira[0]

            while elemento.pai is not None:
                # Insere movimentos efetuados em uma lista para retornar
                movimentos.insert(0, elemento.acao)
                elemento = elemento.pai

            return movimentos

        # Expande o primeiro elemento do heap
        novosEstados = expande(fronteira[0])

        # Para cada novo estado encontrado, inseri-lo no heap se já não tiver sido explorado posteriormente
        for item in novosEstados:
            if item.estado not in explorados:
                novoItem = Nodo(item.estado, item.pai, item.acao,
                                item.custo + calcula_heuristica_manhattan(item.estado))
                insere_min_heap(novoItem, fronteira)

        # Adicionar primeiro elemento do heap na lista de explorados, e removê-lo do heap
        explorados.add(fronteira[0].estado)
        remove_primeiro_min_heap(fronteira)


def calcula_heuristica_manhattan(estado):
    distHeuristica = 0

    for num in range(1, 9):
        # Faz um somatório da distância manhattan de cada peça numérica do seu destino
        distHeuristica += calcula_distancia_manhattan(estado, num)

    # Soma também o espaço em branco e retorna
    return distHeuristica + calcula_distancia_manhattan(estado, '_')


def calcula_distancia_manhattan(estado, numero):

    # Encontra posição do elemento na string
    pos = estado.index(str(numero))

    if(numero == '_'):                                              # Calcula posição alvo do elemento
        posAlvo = 8
    else:
        posAlvo = numero - 1

    # Conta número de movimentos horizontais de distância do alvo
    movHor = abs(pos % 3 - posAlvo % 3)
    # Conta número de movimentos verticais de distância do alvo
    movVert = abs(math.floor(pos / 3) - math.floor(posAlvo / 3))

    # Retorna total de movimentos
    return movHor + movVert


def insere_min_heap(elemento, heap):

    # Insere elemento na última posição do heap
    heap.append(elemento)
    # Salva a posição do novo elemento
    pos = len(heap) - 1

    # Encontra a posição do pai do elemento novo
    posPai = math.floor((pos - 1) / 2)

    # Enquanto o elemento novo for menor que seu pai, efetua um swap entre os dois
    while pos != 0 and elemento.custo < heap[posPai].custo:
        heap[pos], heap[posPai] = heap[posPai], heap[pos]

        # Nova posição do elemento é igual à do pai antigo, se foi efetuada a troca
        pos = posPai
        # Encontra um novo pai
        posPai = math.floor((pos - 1) / 2)


def remove_primeiro_min_heap(heap):

    if len(heap) == 0:
        return

    # Remove a raiz do heap e a substitui pelo último elemento
    heap[0] = heap[-1]
    heap.pop()                                          # Remove o último elemento

    # Salva a posição do elemento na raiz
    pos = 0

    # Checa se a raiz removida não era o único elemento
    if len(heap) > 0:
        while True:                                     # Em um loop, troca o elemento na raiz por seus filhos menores
            posFilhoEsq = (pos + 1) * 2 - 1
            # Se o elemento não tem um filho à esquerda, ele já está na posição correta
            if posFilhoEsq > len(heap) - 1:
                break

            posFilhoDir = (pos + 1) * 2
            if posFilhoDir > len(heap) - 1:
                posFilhoDir = None

            if posFilhoDir is not None:                 # Se o elemento tem um filho à direita, ambos filhos devem ser checados
                # Encontra a posição do menor filho
                posMenorFilho = posFilhoEsq if heap[posFilhoEsq].custo < heap[posFilhoDir].custo else posFilhoDir

                # Se o elemento for maior que pelo menos um dos filhos, efetuar um swap com o menor filho
                if heap[pos].custo < heap[posMenorFilho].custo:
                    # Se o elemento for menor que os dois filhos, ele já está na posição correta
                    break
                else:
                    heap[pos], heap[posMenorFilho] = heap[posMenorFilho], heap[pos]
                    pos = posMenorFilho

            else:
                # Se o elemento só tiver um filho à esquerda, checar se ele é maior
                if heap[pos].custo < heap[posFilhoEsq].custo:
                    # Se o elemento for menor, ele já está no lugar certo
                    break
                else:
                    heap[pos], heap[posFilhoEsq] = heap[posFilhoEsq], heap[pos]
                    break


def achaCaminho(nodo):
    caminho = []
    caminho.append(nodo.acao)
    nodoAux = nodo.pai

    while nodoAux.pai != None:
        # Enquanto no nó raíz, insere a ação no inicio da lista
        caminho.insert(0, nodoAux.acao)
        nodoAux = nodoAux.pai
    return caminho

def calcula_heuristica_hamming(estado):
    
    u=zip(estado,"12345678_")

    distancia = 0

    for i,j in u:
        if i!=j:
            distancia += 1

    return distancia  

