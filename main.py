import tkinter as tk
from tkinter import *
from tkinter import messagebox
from codification_qrcode import codification



root = tk.Tk()
root.title('Gerador de QRCODE')
root.geometry('600x250')
root.configure(background='#000000')


margin = Canvas(root, width=600, bg='#FFFFFF', height=5, bd=1, highlightthickness=1, relief='ridge')
margin.pack()

label_inserir_qr_code = Label(root, bg='#000000', fg='#FFFFFF', text='Inserir link:', font=('Montserrat', 12, 'bold'))
label_inserir_qr_code.pack(pady=10)
labelbox_link = tk.Entry(root, width=60)
labelbox_link.pack(pady=1)

label_inserir_descricao = Label(root, bg='#000000', fg='#FFFFFF', text='Inserir descrição do QRCODE (sem espaço):', font=('Montserrat', 12, 'bold'))
label_inserir_descricao.pack(pady=10)
labelbox_descricao = tk.Entry(root, width=60)
labelbox_descricao.pack(pady=1)

def gerarQRCODE():
    datauser = labelbox_link.get()
    descri = labelbox_descricao.get()

    codification(datauser, descri)

botao_gerar = Button(root, text='Gerar QRCODE', width=15, font=('Montserrat', 12, 'bold'), command=gerarQRCODE)
botao_gerar.configure(bg="#808080", fg="black", relief="raised", padx=10, pady=5, activebackground="#808080")
botao_gerar.pack(pady=30)


root.mainloop()