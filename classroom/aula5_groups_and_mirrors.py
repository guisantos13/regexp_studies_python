import re
from pprint import pprint

# Metacaracters         ^ $ ( )


texto = " <p>Frase</p> <p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div>Frase 4</div>"

# Os quantificadores sempre são aplicados a "coisa" que estiver a esquerda do quantificador.

# GRUPOS (abc|def) encontra uma sequencia de caracteres, diferentemente dos conjuntos.
tags = re.findall(r"(<([pdiv]{1,3})>(.*?)<\/\2>)", texto)
pprint(tags)

for tag in tags:
    grupo_um,grupo_dois,grupo_tres = tag
    print(grupo_tres)

# ?:    ELIMINA A APRESENTAÇÃO DE UM GRUPO DESNECESSÁRIO.
cpf = '097.894.356-22'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# Envolvendo o texto das tags com aspas.
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto))





