from PIL import Image
import os

lista_arquivos = os.listdir('Imagens')

for arquivo in lista_arquivos:

    imagem = Image.open(f'Imagens/{arquivo}')
    imagem.save(f'pdf/{arquivo.replace("jpg", "pdf")}')

