# SorteadorDestinos
Sorteie itens de raridades diferentes com porcentagens dinamicas e com garantia de não haver sorteios repetidos.

<h1>Feito em Python 3</h1>

<h2>Descrição 💻</h2>
Esse projeto visa realizar uma leitura em um arquivo .txt, e carregar esses dados que tem raridades especificas para serem sorteados. O diferencial desse projeto é que a porcentagem de uma raridade ser sorteada muda conforme é realizado os sorteios. Se uma raridade é sorteada, a chance dela ser sorteada diminui e a de outras raridades aumentam, para assim garantir que nunca haja um acumulo grande de itens sorteados da mesma raridade. Há um tratamento no código para que mesmo diminuindo, se houver itens ainda daquela raridade a chance dela ser sorteada nunca chegue a zero. O item que é sorteado é removido e não pode ser sorteado novamente.

Bibliotecas utilizadas:
- random

<h2>Como rodar 👨‍💻</h2>
Basta ter o python 3 instalado em sua maquina, e garantir que o arquivo "destinos.txt" esteja no mesmo
diretorio do código.Esse arquivo é o que irá carregar os itens a serem sorteados no programa, tendo cinco
tipos de raridades distintas.Caso queira alterar os destinos para outro tipo de dado a ser sorteado, é só incluir nesse arquivo ou substituir o nome do arquivo no "SorteadorRaridadeDestinos.py". Existem palavras reservadas no arquivo .txt, que são: incomum, raro, epico, lendario e end. Sendo que o primeiro bloco de dados não tem uma palavra reservada mas contem os destinos de raridade comum. Segue o exemplo do arquivo:

- lista de destinos comuns aqui
- ...
incomum
- lista de destinos incomuns aqui
- ...
raro
- lista de destinos raros aqui
- ...
epico
- lista de destinos epicos aqui
- ...
lendario
- lista de destinos lendarios aqui
- ...
end

Autor:<br>
<a href="https://github.com/JoabUrbano">Joab Urbano</a><br>
