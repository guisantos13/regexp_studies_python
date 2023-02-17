import re

# FLAGS 
# re.I  -> IGNORECASE
# re.A  -> TABELA ASCII
# re.M  -> MULTILINE
# re.S  -> DOTALL

texto = '''
111.293.003-87 112.409.003-94 392.998.223-58
'''

print(re.findall(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}', texto, flags=re.M))

texto2 = 'O João gosta de folia \n e adora ser amado'

# re.S faz com que o . ignore a quebra de linha
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))


