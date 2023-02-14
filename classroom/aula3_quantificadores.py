import re

# Metacaracters         ^ $ * + ? { }  \ ( )


lord_of_the_ring = "Em uma terra fantástica e única, um hobbit recebe de presente de seu tio um anel mágico\
e maligno que precisa ser destruído antes que caia nas mãos do mal.\
Para isso, o hobbits Frodo tem um caminho árduo pela frente, onde encontra perigo, medo e seres bizarros.\
Ao seu lado para o cumprimento desta jornada, ele aos poucos pode contar com outros hobbbbbbbbbbbitsssssss, um elfo, um anão, dois humanos e um mago,\
totalizando nove seres que formam a Sociedade do Anel."

# Os quantificadores sempre são aplicados a "coisa" que estiver a esquerda do quantificador.

# + REPRESENTA 1 OU N REPETIÇÕES
print(re.findall(r"hob+its+", lord_of_the_ring, flags=re.I))

# * REPRESENTA 0 OU N REPETIÇÕES
print(re.findall(r"hobbit[s]*", lord_of_the_ring, flags=re.I))

# ? REPRESENTA 0 OU 1

# {n} EXEMPLOS: {10} REPRESENTA 10 REPETIÇÕES, {10,} REPRESENTA 10 OU MAIS, {,10} REPRESENTA ATÉ 10.
