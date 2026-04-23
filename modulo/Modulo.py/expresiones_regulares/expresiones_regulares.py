import re

texto = "Mi correo es ana@gmail.com y tengo 25 años"

print(re.search(r"\d+", texto))      # Primera coincidencia
#print(re.findall(r"\d+", texto))     # Todas las coincidencias -> ['25']
#print(re.match(r"\w+", texto))       # Solo al inicio del texto
#print(re.sub(r"\d+", "##", texto))   # Reemplazar coincidencias
#print(re.split(r"\s+", texto))       # Dividir por patrón