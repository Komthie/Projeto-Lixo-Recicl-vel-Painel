from tkinter import *
import os
from tkinter import filedialog
from tkinter import Toplevel
import datetime


def reciclaveis():
    lista = ['Garrafas', 'Copos',
    'Embalagens Pet','Refrigerantes'
    ,'Vinagre',
    'Oléo',
    'Sacos',
    'Sacolas',
    'Tampas',
    'Tampas de Garrafa'
    'Latas'
    'Frascos de produtos',
    'Caneta',
    'Canos',
    'Tubos de PVC',
    'Embalagens de produto de limpeza',
    'Embalagens tipo Tupperware',
    'Brinquedos de plástico',
    'Baldes',
    'Frascos de remédio vazio',
    'Potes de conserva',
    'Cacos',
    'Garrafas',
    'Plástico',
    'Copos de plásticos',
    "Canudos de plástico",
    "Talheres de plástico",
    "Pratos de plástico",
    "Embalagens de fast food",
    "Garrafas plásticas",
    "Sacos plásticos",
    "Embalagens de doces",
    "Embalagens de salgadinhos",
    "Embalagens de biscoitos",
    "Embalagens de sorvete",
    "Embalagens de margarina",
    "Embalagens de iogurte",
    "Potes de plástico",
    "Garrafas de vidro",
    "Latas de alumínio",
    "Embalagens de papel",
    "Caixas de pizza",
    "Guardanapos usados",
    "Toalhas de papel",
    "Filtros de café",
    "Sacos de papel",
    "Tubos de pasta de dente",
    "Escovas de dente",
    "Escovas de cabelo",
    "Preservativos",
    "Absorventes íntimos",
    "Fraldas descartáveis",
    "Lenços umedecidos",
    "Papel higiênico usado",
    "Curativos",
    "Fitas adesivas",
    "Embalagens de remédios",
    "Pilhas e baterias",
    "CDs e DVDs",
    "Cartuchos de tinta",
    "Fósforos",
    "Palitos de dente",
    "Espumas de embalagens",
    "Isopor",
    "Canetas esferográficas",
    "Marcadores",
    "Lápis de plástico",
    "Borrachas",
    "Embalagens de cigarros",
    "Bitucas de cigarro",
    "Embalagens de chicletes",
    "Embalagens de balas",
    "Embalagens de chocolates",
    "Papel alumínio",
    "Embalagens de cosméticos",
    "Pincéis descartáveis",
    "Guardanapo"
    "Embalagens de lanches",
    "Copos de café descartáveis",
    "Embalagens de take-away",
    "Garrafas de água descartáveis",
    "Embalagens de fast food",
    "Tubos de creme dental",
    "Escovas de cabelo",
    "Fones de ouvido descartáveis",
    "Cartões de crédito vencidos",
    "Roupas íntimas descartáveis",
    "Máscaras descartáveis",
    "Luvas de plástico descartáveis",
    "Embalagens de produtos de limpeza",
    "Sacolas de supermercado",
    "Cotonetes de plástico",
    "Cotonetes de plásticos"
    "Talheres de plástico",
    "Pratos de papel",
    "Embalagens de delivery",
    "Potes de comida pronta",
    "Embalagens de macarrão instantâneo",
    "Embalagens de congelados",
    "Sacolas de entrega de delivery",
    "Potes de plástico de manteiga",
    "Canetas esferográficas vazias",
    "Raspadinhas",
    'Copo de suco'
    "Pratinhos de festa descartáveis",
    "Envelopes de carta",
    "Embalagens de fast food",
    'Papel'
    'Canudos'
    'Sacolas'
    'Copos de plástico'
    'Copos de plastico'
             ]
    palavra = entrada.get()
    if palavra in lista:
        txt.delete('1.0', END)
        txt.insert(END, f'O Objeto {palavra} é Descartável/Reciclavél!\nVerifique de lavar bem este objeto antes de descarta-lo.\n Obrigado!')
    else:
        txt.delete('1.0', END)
        txt.insert(END, f'O Objeto {palavra} Não é reciclável.\n Lembre-se de Verificar o melhor local para o seu Descarte!')
def open_file():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Resíduos e Informações", filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")))
    if filename:
        with open(filename, 'r') as file:
            content = file.read()
        file_window = Toplevel(janu)
        file_window.title("Importãncia do destino correto do lixo")
        text_widget = Text(file_window, height=20, width=100, background='#07FBA6', font=('Arial',14))
        text_widget.insert(END, content)
        text_widget.pack()

def mostrar_horario():
    horario_atual = datetime.datetime.now().strftime('%H:%M:%S')
    horario_label.config(text=horario_atual, bg='#E507FB')
    janu.after(1000, mostrar_horario)


janu = Tk()
janu.title('Descarte de Resíduos')
janu.geometry('520x450')
janu.iconbitmap('')
janu.resizable(False, False)
janu.configure(background='#FBFF04')

cred = Button(janu, text='P.Konorath', bg='#07F7FB', fg='#000', font=('Arial', 13))
cred.place(x=417, y=32)

cred2 = Button(janu, text='G. Blasio', bg='#C707FB', fg='#000', font=('Arial', 13))
cred2.place(x=320, y=32)

sair_botao = Button(janu, text='Sair', bg='red', fg='white', font=('Arial', 12), command=janu.quit)
sair_botao.place(x=115, y=32)

saiba_mais = Button(janu, text='Saiba mais!', bg='brown', fg='white', font=('Arial', 12), command=open_file)
saiba_mais.place(x=5, y=32)

executar = Button(janu, text='Pesquisar', bg='#3FFA22', fg='#000', height=1, font=('Arial', 12), command=reciclaveis)
executar.place(x=417, y=0)

entrada = Entry(janu, bg='white', fg='black', width=45, font=('Arial', 13))
entrada.place(x=5, y=5)

ajuda = Label(janu, text='Descubra a melhor maneira de descartar seu Lixo!', fg='#FFF', bg='#2604FF', font=('Arial', 14), width=50)
ajuda.place(x=2, y=70)

txt = Text(janu, background='#FB8507', height=19, font=('Arial', 14), fg='#FFF')
txt.place(x=1, y=100)


horario_label = Label(janu, text='', font=('Arial', 18))
horario_label.place(x=190,y=32)

mostrar_horario()

janu.mainloop()
