# SorteadorDestinos
Faz a leitura de um arquivo e faz o sorteio da raridade e qual caracteristica ele terá. Nenhuma caracteristica pode ser ganha mais de uma vez.

<h3>Feitoo em Python 3</h3>

Bibliotecas utilizadas:
- time
- random

O arquivo tem nome de "destinos.txt", caso queira alterar os destinos para outro tipo de dado a ser sorteado é só colocar nesse arquivo ou substituir
o nome do arquivo no SorteadorRaridadeDestino. Existem palavras reservadas no arquivo .txt, que são: incomum, raro, epico, lendario e end. Sendo que o
primeiro bloco de dados não tem uma palavra reservada mas contem os destinos de raridade comum. Segue o exemplo do arquivo:

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
