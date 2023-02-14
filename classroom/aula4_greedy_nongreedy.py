import re

# Metacaracters         ^ $ * + ? { }  \ ( )


texto = " <p> Frase </p> <p> Frase 1 </p> <p> Frase 2 </p> <p> Frase 3 </p> <div> Frase 4 </div>"

# Os quantificadores sempre são aplicados a "coisa" que estiver a esquerda do quantificador.

# GREEDY ele verifica toda a sentença e retorna todo o valor presente até a ultima passagem em que ela foi fechada.
print(re.findall(r"<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>", texto))

# NON-GREEDY ele verifica a sentença e retorna os valores a cada vez que ela é fechada , para esse comportamento utilizamos a ? após o quantificador *.
print(re.findall(r"<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>", texto))



