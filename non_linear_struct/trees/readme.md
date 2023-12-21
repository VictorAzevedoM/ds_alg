# Árvore Binária

Inserção (Insertion):

    A inserção em uma Árvore Binária começa no nó raiz.
    Se a árvore estiver vazia, o novo elemento se torna o nó raiz.
    Se a árvore não estiver vazia, o novo elemento é comparado com o nó atual.
    Se o novo elemento for menor que o nó atual, ele é inserido à esquerda do nó atual se houver espaço vazio; caso contrário, a inserção continua recursivamente na subárvore esquerda.
    Se o novo elemento for maior que o nó atual, ele é inserido à direita do nó atual se houver espaço vazio; caso contrário, a inserção continua recursivamente na subárvore direita.
    O processo continua até encontrar um espaço vazio para inserir o novo nó.

Traversal (Travessia):

Existem três principais métodos de travessia em uma Árvore Binária:

    Inorder Traversal:
        Visita os nós na ordem esquerda-raiz-direita.
        Para uma árvore de busca binária, os valores visitados são impressos em ordem crescente.

    Preorder Traversal:
        Visita o nó raiz antes de visitar seus filhos.
        Utilizado para criar uma cópia da árvore ou expressar a árvore em notação polonesa.

    Postorder Traversal:
        Visita os filhos antes de visitar o nó raiz.
        Usado para deletar a árvore ou expressar a árvore em notação polonesa reversa.

Busca (Search):

    A busca em uma Árvore Binária começa no nó raiz.
    O elemento a ser buscado é comparado com o valor do nó atual.
    Se o elemento for igual ao valor do nó atual, o elemento foi encontrado.
    Se o elemento for menor que o valor do nó atual, a busca continua recursivamente na subárvore esquerda.
    Se o elemento for maior que o valor do nó atual, a busca continua recursivamente na subárvore direita.
    O processo continua até encontrar o elemento ou percorrer todos os nós e constatar que o elemento não está presente.

Remoção (Deletion):

    A remoção de um nó em uma Árvore Binária envolve diferentes casos, como nó folha, nó com um filho ou nó com dois filhos.
    A complexidade da remoção envolve a manutenção da estrutura da árvore após a remoção do nó desejado, garantindo que a propriedade da Árvore Binária seja mantida.

Esses conceitos básicos abordam o funcionamento fundamental de uma Árvore Binária em termos de inserção, travessia, busca e remoção. Cada operação possui suas próprias complexidades e considerações, que podem variar dependendo da implementação específica ou da estrutura da árvore em questão.