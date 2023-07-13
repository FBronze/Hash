#!/usr/bin/python
import hashlib
from Cryptodome.Hash import MD2
import sys

# Verifica se foram fornecidos os argumentos corretos
if len(sys.argv) != 3:
    print("Uso: python script.py <arquivo> <hash>")
    sys.exit(1)

arquivo = sys.argv[1]
hash_desejado = sys.argv[2]

with open(arquivo, "r") as file:
    for line in file:
        crip = line.strip()
        # Mude conforme a necessidade
        md2_hash = MD2.new(crip.encode()).hexdigest()
        md5_hash = hashlib.md5(crip.encode()).hexdigest()
        md4_hash = hashlib.new("md4", crip.encode()).hexdigest()

        if md2_hash == hash_desejado:
            print(crip)
        elif md5_hash == hash_desejado:
            print(crip)
        elif md4_hash == hash_desejado:
            print(crip)

print("===== Finalizado =====")
