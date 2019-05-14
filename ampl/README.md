## AMPL

Ao longo do  curso, utilizamos o software de otimização AMPL. A vantagem dessa linguagem é que permite separarmos completamente os dados (`.dat`) do modelo (`.mod`). Além disso, a sintaxe é muito semelhante à descrição matemática que utilizamos para modelar o problema. Alguns dos exercícios resolvidos em AMPL encontram-se nessa pasta.

### Lista de exercícios

Livro: [A Gentle Introduction to Optimization](https://www.cambridge.org/br/academic/subjects/mathematics/optimization-or-and-risk-analysis/gentle-introduction-optimization?format=HB&isbn=9781107053441)

- Capítulo 1: Exercícios 2, 3 e 4 (`PO1L1E*`)
- Capítulo 2: Exercícios 3, 5 e 7 (`PO1L2E*`)

Livro: [Applied Mathematical Programming](http://web.mit.edu/15.053/www/AMP.htm)
- Capítulo 9: Exercício 4 (`PO1L9E4`)

Os demais exercícios (`PO1transport`, `PO1network`) foram propostos em aula.

### Como rodar? 

#### Instalar ampl
Caso você não possua o software, você pode baixar [aqui](https://ampl.com/try-ampl/download-a-free-demo/).

#### Movendo os arquivos
Você pode passar os arquivos para a pasta do AMPL, `ampl/models` (no meu caso, a pasta foi salva como `ampl.macosx64/models`), com o seguinte comando:

```
$ cd [PATH_TO_FOLDER]/FGV_PO1/ampl
$ mv PO1* [PATH_TO_AMPL]/models
```

#### Rodando os arquivos
Para rodar um arquivo, basta executar o `.run` referente ao mesmo, da seguinte forma:

```
$ cd PATH/TO/ampl_FOLDER;
$ ./ampl;
$ ampl: option ampl_include models;
$ ampl: include [YOUR_FILENAME].run;
```
