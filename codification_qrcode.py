import qrcode
import time
from PIL import Image
import os


# CODIFICANDO
def codification(data_user, descricao):

    diretorio_padrao = os.path.join(os.path.expanduser('~'), 'Documentos')

    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    qr.add_data(data_user)

    qr.make(fit=True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')

    caminho_arquivo = os.path.join(diretorio_padrao, f'{descricao}.png')

    img.save(os.path.join(caminho_arquivo))

    time.sleep(0.5)

    image = Image.open(caminho_arquivo)

    image.show()
