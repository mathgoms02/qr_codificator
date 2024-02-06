import qrcode
import time
from PIL import Image

def codification(data_user, descricao):
    # CODIFICANDO
    # data_user = input("Insira um link para se tornar um QRCode: ")
    # descricao = input("Nome pro qrcode (sem espaço): ")
    # img = qrcode.make(data)
    # img.save('C:/Users/matgo/OneDrive/Documentos/UDEMY/Python/diversos/qrcode/imagem/myqrcode.png')

    image_path = f'C:/Users/matgo/OneDrive/Documentos/UDEMY/Python/diversos/qrcode/imagem/{descricao}.png'

    #############################################################################################################################################################################################

    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    qr.add_data(data_user)

    qr.make(fit=True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')

    img.save(f'C:/Users/matgo/OneDrive/Documentos/UDEMY/Python/diversos/qrcode/imagem/{descricao}.png')

    time.sleep(0.5)

    image = Image.open(image_path)

    image.show()

#############################################################################################################################################################################################

