Filas

A regra que determina quem é o próximo da fila chama-se política de enfileiramento.
A política de enfileiramento mais simples chama-se FIFO, sigla de first-in-first-out:
primeiro a entrar, primeiro a sair. A política de enfileiramento mais geral é o
enfileiramento por prioridade, em que se atribui uma prioridade a cada pessoa da
fila e a que tiver maior prioridade vai primeiro, independente da sua ordem de chegada.

O TDA Fila e o TDA Fila por Prioridade têm o mesmo conjunto de operações.
A diferença está na semântica das operações: a fila usa a política FIFO; e a fila
por prioridade (como o próprio nome sugere) usa a política de enfileiramento por prioridade.

-------------------------------------------------------------------------------------
O TDA Fila é definido pelas seguintes operações:

__init__
Inicializar uma nova fila vazia.

insert
Adicionar um novo item à fila.

remove
Remover e retornar um item da fila. O item retornado é o que foi adicionado primeiro.

isEmpty
Checar se a fila está vazia.