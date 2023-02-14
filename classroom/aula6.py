import re


# METACARACTERES         ^ $ 

# ^    INDICA COMEÇA COM
# $    INDICA TERMINA COM
# [^A-Z] INDICA QUALQUER COISA QUE NÃO ESTEJA ENTRE A-Z


cpf = '097.894.356-22'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^a-z]+', cpf))



