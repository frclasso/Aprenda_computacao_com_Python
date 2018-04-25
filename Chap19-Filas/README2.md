O TDA Fila por Prioridade tem a mesma interface que o TDA Fila, mas semântica diferente.

Mais uma vez, a interface é a seguinte:

__init__
Inicializar uma nova fila vazia.

insert
Adicionar um novo item à fila.

remove
Remover e retornar um item da fila. O item retornado é aquele que tiver maior prioridade.

isEmpty
Checar se a fila está vazia.

A diferença semântica é que o item removido da fila não é necessariamente o que foi incluído
primeiro e, sim, o que tem maior prioridade. Que prioridades são essas e como elas se comparam
umas com as outras não é especificado pela implementação Fila por Prioridade.
Isso depende de quais itens estão na fila.

Por exemplo, se os itens da fila tiverem nome, podemos escolhê-los por ordem alfabética.
Se for a pontuação de um jogo de boliche, podemos ir da maior para a menor, mas se for
pontuação de golfe, teríamos que ir da menor para a maior. Se é possível comparar os itens
da fila, é possível achar e remover o que tem maior prioridade. Essa implementação da Fila
por Prioridade tem como atributo uma lista Python chamada items, que contém os itens da fila.