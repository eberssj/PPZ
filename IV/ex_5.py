text = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()

import string
text = text.replace('.', ' ')
text = text.replace(',', ' ')
lista = []

def letra_python(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False

for p in text.split():
    if letra_python(p) and len(p) > 4:
        lista.append(p)
   
print(f'Lista: {lista}')
print(f'Quantidade de palavras: {len(lista)}')




