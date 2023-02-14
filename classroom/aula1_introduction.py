import re

# Aula 1

# search

var_regex = "Teste de expressões regulares."
print(re.search(r"Teste", var_regex))

# findall

print(re.findall(r"Teste", var_regex))

# sub

print(re.sub(r"Teste", "ABC", var_regex))

# compile

regexp = re.compile(r"Teste")
print(regexp.findall(var_regex))
print(regexp.search(var_regex))
print(regexp.sub("123", var_regex))
