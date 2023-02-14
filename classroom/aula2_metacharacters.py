import re

# Metacaracters        . ^ $ * + ? { } [ ] \ | ( )


lord_of_the_ring = "Em uma terra fantástica e única, um hobbit recebe de presente de seu tio um anel mágico\
e maligno que precisa ser destruído antes que caia nas mãos do mal.\
Para isso, o hobbit Frodo tem um caminho árduo pela frente, onde encontra perigo, medo e seres bizarros.\
Ao seu lado para o cumprimento desta jornada, ele aos poucos pode contar com outros hobbits, um elfo, um anão, dois humanos e um mago,\
totalizando nove seres que formam a Sociedade do Anel."

# |  significa OU
# .  significa QUALQUER CARACTERE (COM EXCEÇÃO DA QUEBRA DE LINHA)
print(re.findall(r"hobbit|.nel", lord_of_the_ring))

# [] significa CONJUNTO DE CARACTERES
print(re.findall(r"[a-z|A-Z]nel", lord_of_the_ring))

# Flags IGNORECASE
print(re.findall(r"anel", lord_of_the_ring, flags=re.I))
