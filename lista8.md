#### 1. Defina algoritmo eficiente. Defina problema de decisãoo. Defina verificador polinomial para sim. Defina verificador polinomial para nao˜ . Defina as classes P, NP e coNP. Dˆe um exemplo de um problema em cada uma dessas classes, justificando a sua pertinˆencia `a classe.
##### Algoritmo Eficiente
Algoritmo é um algoritmo que tem consumo de tempo O(n^k), onde k é uma
constante. Ou seja, qualquer allgoritmo pelo menos polinomial é eficiente.

##### Problema de Decisão
Um problema de decisão é um problema que pode ser respondido com 'SIM' e 'NÃO'.
Por exemplo, um problema para encontrarmos um caminho hamiltoniano em um grafo G
não é um problema de decisão. No entanto, um problema que pergunta se existe um
caminho hamiltoniano em G, a resposta é 'SIM' ou 'NÃO', portanto, é uma versão
do problema anterior mas modificado para ser um problema de decisão.

##### Verificador polinomial para 'SIM'
Um verificador polinomial é um algoritmo polinomialque verifica um outro
algoritmo. Suponha que temos um algoritmo A que resolve um problema de decisão.
Para verificarmos a validade da repsosta de A, podemos fazer A retornar um
'certificado' junto com sua resposta (SIM/NÃO). Assumindo que A é um algortimo
que resolve o problema de "Existe um caminho hamiltoniano em G" se A retorna
SIM/NÃO e o certificado, que pode ser um caminho hamiltoniano dentro de G.

valida o certificado recebido de A, ou seja, testa se o caminho recebido
Um verificador polinomial para 'SIM' nesse caso é um algoritmo polinomial que
realmente é um caminho hamiltoniano em G.

Um verificador polinomial para a resposta SIM a um problema P é um algoritmo
polinomial ALG que recebe a instância I de um P, um objeto C e devolve:
- SIM para algum C se a resposta P(I) é SIM.
- NÃO para todo C se a resposta a P(I) é NÃO.

##### Verificador polinomial para 'NÃO'

Um verificador polinomial para 'NÃO' é um algoritmo polinomial ALG para um
problema de decisão P e instância I de P, um objeto C e devolve:
- SIM para algum C se a resposta de P(I) for NÃO.
- NÃO para todo C se a resposta de P(I) for SIM.

#### Classe P
A classe P é a classe de todos os problemas de decisão que podem ser resolvidos
por algoritmos que tem consumo de tempo O(n^k), onde k é uma constante. Ou seja,
a classe de problemas de decisão que podem ser resolvidos por no máximo
algoritmos polinomiais.

Um exemplo de problema da classe P é: Saber se um número está numa lista. O
algoritmo que resolve o problema é O(N), onde N é o tamanho da lista, já que é
necessário somente percorrer a lista em busca do número.

#### Classe NP
Um problema da classe NP é um problema de decisão P que tem um algoritmo
polinomial ALG que é verificado polinomial para SIM..

Exemplo: Existe um ciclo hamiltoniano no grafo G. Um verificador polinomial ALG'
do problema que tem um algoritmo ALG  só precisa checar se o caminho retornado
por ALG é um caminho hamiltoniano válido ou não. ALG' portanto é O(N), onde N é
o número de vértices de grafo G.

#### Classe coNP
A classe coNP contém problemas de decisão que tem um verificador polinomial para
NÃO.

Exemplo: problema de insatisfatibilidade: checar se não existe como satisfazer
uma fórmula booleana. Assim como seu problema irmão NP, Sat, esse problema
também tem um verificador polinomial, mas para não.

#### 2. Mostre que SAT está em NP. (Essa é a parte fácil do teorema de Cook.)
SAT está em NP pois o algoritmo ALG' verificador do algoritmo ALG que resolve o
problema de SAT P só precisa validar o certificado retornado por ALG, ou seja: o
algoritmo ALG' recebe a combinação de valores das variáveis em ALG que fez a
condição se tornar verdade, o algoritmo então pega essa combinação e testa. Por
fim, isso é O(N) onde N é a quantidade de variáveis.

#### 3. Uma fórmula booleana C sobre um conjunto X de variáveis booleanas (não necessariamente em CNF) é uma tautologia se toda atribuicão a X satisfaz C. O problema tautologia consiste em, dado X e C, decidir se C é ou não uma tautologia. Prove que o problema tautologia está em coNP.


Quando recebemos o SIM não tem nada a se fazer, já que C é verdadeiro pra todas
elas. Quando recebemos NÃO, podemos provar com uma fórmula booleana C que fazem
C ser falso para algum X. Com isso, pode-se usar o problema de UNSAT, que é
coNP, que checa se a fórmula C é insatisfeita, se sim, conseguimos provar que C
não é uma tautologia. Como ele reduz o problema de tautologia à unsat, que é
coNP, temos que o problema de tautologia também é coNP.

#### 4. O problema 2-sat consiste na restrição de sat a instâncias X e C em que toda cláusula de C tem exatamente dois literais. Mostre que o 2-sat está em P, ou seja, descreva um algoritmo polinomial que resolva o 2-sat.


Uma formula (A or B) pode ser entendida como:
~A => B e ~B => A.

Se criarmos um grafo G com os vértices X e ~X onde X é cada variavel, teremos um
grafo com as interações entre as variáveis. Se uma variável X tiver um caminho
para sua negação ~X e ~X tiver um caminho para X, pode-se concluir que C é
insatisfeito pois não tem nenhum caso para satisfazer a fórmula. Com o grafo G
criado é necessário identificar todos os componentes conexos do grafo. Pode-se
usar o algoritmo de Kosaraju-Sharir que acha os componentes conexos do grafo e
os retorna. Com isso, pode-se validar se não existe nenhum vértice X e ~X em um
mesmo componente conexo. Com isso, é possível definir se é satisfatível ou não.

A complexidade desse algoritmo seria O(C) para gerar o grafo e O(G) para
executar o algortimo de Kosaraku-Sharir. Portanto, 2-sat pertence a classe P.

#### 5. Seja G = (V, E) um grafo. Um conjunto S ⊆ V é independente se quaisquer dois vértices de S não são adjacentes. Ou seja, não há nenhuma aresta do grafo com as duas pontas em S. O problema IS consiste no seguinte: dado um grafo G e um inteiro k ≥ 0, existe um conjunto independente em G com k vértices? Mostre que o problema IS é NP-completo.