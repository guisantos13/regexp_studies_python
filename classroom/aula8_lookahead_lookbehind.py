import re


texto = '''
ONLINE  192.168.0.1 GHIJK ACTIVE 
OFFLINE 192.168.0.2 GHIJK ACTIVE
OFFLINE 192.168.0.3 GHIJK INACTIVE
ONLINE  192.168.0.4 GHIJK INACTIVE
ONLINE  192.168.0.5 GHIJK ACTIVE
'''

# Positive lookahead
print("Positive lookahead:", re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=ACTIVE)', texto))

# Negative lookahead
print("Negative lookahead:", re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!ACTIVE)', texto))

# Positive lookbehind
print("Positive lookbehind:", re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# nEGATIVE lookbehind
print("Positive lookbehind:", re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))