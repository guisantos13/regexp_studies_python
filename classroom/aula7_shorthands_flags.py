import re


lord_of_the_ring = """Em uma terra fantástica e única, um hobbit recebe de presente de seu tio um anel mágico
e maligno que precisa ser destruído antes que caia nas mãos do mal.
Para isso, o hobbit Frodo tem um caminho árduo pela frente, onde encontra perigo, medo e seres bizarros.
Ao seu lado para o cumprimento desta jornada, ele aos poucos pode contar com outros 3 hobbits, um elfo, um anão, dois humanos e um mago,
totalizando 9 seres que formam a Sociedade do Anel."""

#print(re.findall(r'[a-zA-Z0-9À-ú]+', lord_of_the_ring))

# \w representa [a-zA-Z0-9À-ú_]   - Obs: Sempre que quiser fazer a negação basta informar a letra maíscula ex: \W
print(re.findall(r'\w+', lord_of_the_ring))

# \d representa digitos de 0-9    - Obs: Sempre que quiser fazer a negação basta informar a letra maíscula ex: \D
print(re.findall(r'\d+', lord_of_the_ring))

# \s qualquer tipo de espaço [\ \n \f \t]
print(re.findall(r'\s+', lord_of_the_ring))

# \b encontra a borda e as palavras que começam/terminam com o inicio definido
print(re.findall(r'\be\w+', lord_of_the_ring))
print(re.findall(r'\w+e\b', lord_of_the_ring))

# Econtra palavras que tenham 4 caracteres
print(re.findall(r'\b\w{4}\b', lord_of_the_ring))


