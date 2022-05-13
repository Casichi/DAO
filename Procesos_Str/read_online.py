from urllib.request import urlopen

with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    # contenido = mensaje.read()
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)