#!/usr/bin/python
import hashlib
import sys
import base64

# Verifica se foram fornecidos os argumentos corretos
if len(sys.argv) != 3:
    print("Uso: python script.py <arquivo> <hash>")
    sys.exit(1)

arquivo = sys.argv[1]
hash_desejado = sys.argv[2]

with open(arquivo, "r") as file:
    for line in file:
        crip = line.strip()
        md5_hash = hashlib.md5(crip.encode()).hexdigest()
        base64_hash = base64.b64encode(md5_hash.encode()).decode()
        sha1_hash = hashlib.sha1(base64_hash.encode()).hexdigest()
        
        if sha1_hash == hash_desejado:
            print(crip)

print("===== Finalizado =====")
