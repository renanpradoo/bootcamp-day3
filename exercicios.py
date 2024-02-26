texto = "hoje e nossa segunda aula do bootcamp, bootcamp de python bootcamp"

texto_split = texto.replace(',','')
texto_split = texto_split.split(' ')

texto_count = {}

for palavra in texto_split:
    if palavra in texto_count:
        texto_count[palavra] += 1
    else:
        texto_count[palavra] = 1

print(texto_count)
