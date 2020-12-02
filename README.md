# classificadoresknnperceptron
Uso de classificadores: KNN e Perceptron para classificar variação morfológica das flores de íris de três espécies 
* Trabalho da Disciplina Sistemas Inteligentes feito juntamente com a aluna LUMA SLLARY FERNANDES OLIVEIRA
# KNN
O KNN foi proposto por Fukunaga e Narendra em 1975. É um dos classificadores mais simples de ser implementado, de fácil compreensão e ainda hoje pode obter bons resultados dependendo de sua aplicação
* Significa os K vizinhos mais próximos
* A ideia principal do KNN é determinar o rótulo de classificação de uma amostra baseado nas amostras vizinhas advindas de um conjunto de treinamento.
## Sua classificação é feita da seguinte maneira:
* Inicialmente, calcula-se a distância entre o componente principal e todos os padrões de treinamento.
* Verifica-se quais classes pertencem aos K padrões mais próximos;
* A classificação é feita associando-se o padrão de testa à classe que for mais frequente entre os K padrões mais próximos do componente.

# Perceptron
O perceptron é um tipo de rede neural artificial inventada em 1957 por Frank Rosenblatt no Cornell Aeronautical Laboratory. Ele pode ser visto como o tipo mais simples de rede neural feedforward: um classificador linear.
* Perceptron aprende conceitos, ele pode aprender a responder com verdadeiro (1) ou falso (0) pelas entradas que nós apresentamos a ele, “estudando” repetidamente os exemplos que lhe são apresentados. 
* O perceptron é uma rede neural cujos os pesos e inclinações podem ser treinados para produzir um vetor alvo que quando apresentamos tem que corresponder ao vetor de entrada

# O Problema
* Iris dataset é um conjunto de dados multivariados, introduzido pelo britânico Ronald Fisher, que também é biólogo e estatístico;
* Usado como um exemplo de analise em uso de múltiplas medições em problemas taxonômicos, como analise discriminante linear;
* É uma variação morfológica das flores de íris de três espécies relacionadas;
* Duas das três espécies foram coletadas na Península de Gaspé.
- O conjunto de dados consistem em 50 amostras de cada uma das três espécies, que são:
* Iris setosa;
* Iris virginica;
* Iris versicolor.
- Cada uma com quatro características:
* Comprimento da sépala;
* Largura da sépala;
* Comprimento da pétala;
* Largura da pétala.
