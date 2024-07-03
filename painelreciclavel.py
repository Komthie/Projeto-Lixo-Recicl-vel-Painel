from tkinter import *
import os
from tkinter import filedialog
from tkinter import Toplevel
import datetime


def reciclaveis():
    lista = [
    'Garrafas', 'Copos', 'Embalagens Pet', 'Refrigerantes', 'Vinagre', 'Óleo', 'Sacos', 'Sacolas', 'Tampas',
    'Tampas de Garrafa', 'Latas', 'Frascos de produtos', 'Caneta', 'Canos', 'Tubos de PVC',
    'Embalagens de produto de limpeza', 'Embalagens tipo Tupperware', 'Brinquedos de plástico', 'Baldes',
    'Frascos de remédio vazio', 'Potes de conserva', 'Cacos', 'Plástico', 'Copos de plásticos',
    "Canudos de plástico", "Talheres de plástico", "Pratos de plástico", "Embalagens de fast food",
    "Garrafas plásticas", "Sacos plásticos", "Embalagens de doces", "Embalagens de salgadinhos",
    "Embalagens de biscoitos", "Embalagens de sorvete", "Embalagens de margarina", "Embalagens de iogurte",
    "Potes de plástico", "Garrafas de vidro", "Latas de alumínio", "Embalagens de papel", "Caixas de pizza",
    "Guardanapos usados", "Toalhas de papel", "Filtros de café", "Sacos de papel", "Tubos de pasta de dente",
    "Escovas de dente", "Escovas de cabelo", "Preservativos", "Absorventes íntimos", "Fraldas descartáveis",
    "Lenços umedecidos", "Papel higiênico usado", "Curativos", "Fitas adesivas", "Embalagens de remédios",
    "Pilhas e baterias", "CDs e DVDs", "Cartuchos de tinta", "Fósforos", "Palitos de dente",
    "Espumas de embalagens", "Isopor", "Canetas esferográficas", "Marcadores", "Lápis de plástico", "Borrachas",
    "Embalagens de cigarros", "Bitucas de cigarro", "Embalagens de chicletes", "Embalagens de balas",
    "Embalagens de chocolates", "Papel alumínio", "Embalagens de cosméticos", "Pincéis descartáveis",
    "Guardanapo", "Embalagens de lanches", "Copos de café descartáveis", "Embalagens de take-away",
    "Garrafas de água descartáveis", "Tubos de creme dental", "Fones de ouvido descartáveis",
    "Cartões de crédito vencidos", "Roupas íntimas descartáveis", "Máscaras descartáveis",
    "Luvas de plástico descartáveis", "Cotonetes de plástico", "Pratinhos de festa descartáveis",
    "Envelopes de carta", "Papel", "Canudos", "Copos de plástico", "Potes de plástico de manteiga",
    "Canetas esferográficas vazias", "Raspadinhas", 'Copo de suco', 'Papelão', 'Jornais', 'Revistas',
    'Livros', 'Caixas de papelão', 'Rolos de papel higiênico', 'Rolos de papel toalha', 'Embalagens de ovos',
    'Tampinhas de garrafa', 'Garrafas de vidro de bebidas', 'Garrafas de vidro de alimentos',
    'Potes de vidro', 'Vidros de conserva', 'Vidros de perfume', 'Espelhos', 'Janela de vidro',
    'Telhas de vidro', 'Louças', 'Cerâmica', 'Porcelana', 'Tijolo', 'Concreto', 'Metal', 'Ferro',
    'Aço', 'Alumínio', 'Latas de alumínio', 'Folhas de alumínio', 'Fios de cobre', 'Cabos elétricos',
    'Pilhas', 'Baterias', 'Lâmpadas fluorescentes', 'Lâmpadas LED', 'Tintas', 'Vernizes', 'Óleos',
    'Solventes', 'Pesticidas', 'Agrotóxicos', 'Medicamentos', 'Cosméticos', 'Produtos de higiene pessoal',
    'Plásticos recicláveis', 'PET', 'HDPE', 'PVC', 'LDPE', 'PP', 'PS', 'Poliestireno expandido',
    'Polipropileno', 'Polietileno tereftalato', 'Poliuretano', 'Borracha', 'Madeira', 'Papelão ondulado',
    'Papel kraft', 'Papel reciclado', 'Papelão', 'Cartão', 'Papel higiênico', 'Papel toalha', 'Lenços de papel',
    'Guardanapos de papel', 'Embalagens de papelão', 'Caixas de papelão', 'Sacos de papel', 'Envelopes',
    'Revistas', 'Jornais', 'Livros', 'Cadernos', 'Folhas de papel', 'Cartões postais', 'Cartões de visita',
    'Etiquetas', 'Etiquetas adesivas', 'Fitas adesivas', 'Fitas isolantes', 'Fios de nylon', 'Cordas',
    'Tecidos', 'Roupas', 'Cortinas', 'Toalhas', 'Lençóis', 'Tapetes', 'Carpets', 'Borracha', 'Couro',
    'Peles', 'Penas', 'Ossos', 'Cascos', 'Chifres', 'Conchas', 'Madeira', 'Bambu', 'Palha', 'Cana-de-açúcar',
    'Algodão', 'Lã', 'Seda', 'Linho', 'Juju', 'Sisal', 'Cabelo humano', 'Unhas', 'Dentes', 'Pele',
    'Sangue', 'Fezes', 'Urina', 'Comida', 'Resíduos orgânicos', 'Resíduos industriais', 'Resíduos hospitalares',
    'Resíduos de construção', 'Resíduos eletrônicos', 'Resíduos nucleares', 'Resíduos radioativos',
    'Resíduos perigosos', 'Resíduos tóxicos', 'Resíduos inflamáveis', 'Resíduos corrosivos',
    'Resíduos explosivos', 'Resíduos biológicos', 'Resíduos químicos', 'Resíduos agrícolas',
    'Resíduos florestais', 'Resíduos minerais', 'Resíduos metálicos', 'Resíduos plásticos',
    'Resíduos de papel', 'Resíduos de vidro', 'Resíduos de borracha', 'Resíduos de tecido',
    'Resíduos de couro', 'Resíduos de madeira', 'Resíduos de alimentos', 'Resíduos de bebidas',
    'Resíduos de medicamentos', 'Resíduos de cosméticos', 'Resíduos de produtos de higiene pessoal',
    'Resíduos de embalagens', 'Resíduos de construção e demolição', 'Resíduos de jardinagem',
    'Resíduos de poda', 'Resíduos de folhas', 'Resíduos de galhos', 'Resíduos de troncos',
    'Resíduos de terra', 'Resíduos de areia', 'Resíduos de pedras', 'Resíduos de concreto',
    'Resíduos de asfalto', 'Resíduos de metal', 'Resíduos de plástico', 'Resíduos de papel',
    'Resíduos de vidro', 'Resíduos de borracha', 'Resíduos de tecido', 'Resíduos de couro',
    'Resíduos de madeira', 'Resíduos de alimentos', 'Resíduos de bebidas', 'Resíduos de medicamentos',
    'Resíduos de cosméticos', 'Resíduos de produtos de higiene pessoal', 'Resíduos de embalagens',
    'Resíduos de construção e demolição', 'Resíduos de jardinagem', 'Resíduos de poda',
    'Resíduos de folhas', 'Resíduos de galhos', 'Resíduos de troncos', 'Resíduos de terra',
    'Resíduos de areia', 'Resíduos de pedras', 'Resíduos de concreto', 'Resíduos de asfalto',
    'Resíduos de metal', 'Resíduos de plástico', 'Resíduos de papel', 'Resíduos de vidro',
    'Resíduos de borracha', 'Resíduos de tecido', 'Resíduos de couro', 'Resíduos de madeira',
    'Resíduos de alimentos', 'Resíduos de bebidas', 'Resíduos de medicamentos',
    'Resíduos de cosméticos', 'Resíduos de produtos de higiene pessoal', 'Resíduos de embalagens',
    'Resíduos de construção e demolição', 'Resíduos de jardinagem', 'Resíduos de poda',
    'Resíduos de folhas', 'Resíduos de galhos', 'Resíduos de troncos', 'Resíduos de terra',
    'Resíduos de areia', 'Resíduos de pedras', 'Resíduos de concreto', 'Resíduos de asfalto',
    'Resíduos de metal', 'Resíduos de plástico', 'Resíduos de papel', 'Resíduos de vidro',
    'Resíduos de borracha', 'Resíduos de tecido', 'Resíduos de couro', 'Resíduos de madeira',
    'Resíduos de alimentos', 'Resíduos de bebidas', 'Resíduos de medicamentos',
    'Resíduos de cosméticos', 'Resíduos de produtos de higiene pessoal', 'Resíduos de embalagens',
    'Resíduos de construção e demolição', 'Resíduos de jardinagem', 'Resíduos de poda',
    'Resíduos de folhas', 'Resíduos de galhos', 'Resíduos de troncos', 'Resíduos de terra',
    'Resíduos de areia', 'Resíduos de pedras', 'Resíduos de concreto', 'Resíduos de asfalto',
    'Resíduos de metal', 'Resíduos de plástico', 'Resíduos de papel', 'Resíduos de vidro',
    'Resíduos de borracha', 'Resíduos de tecido', 'Resíduos de couro', 'Resíduos de madeira',
    'Resíduos de alimentos', 'Resíduos de bebidas', 'Resíduos de medicamentos',
    'Resíduos de cosméticos', 'Resíduos de produtos de higiene pessoal', 'Resíduos de embalagens',
    'Resíduos de construção e demolição', 'Resíduos de jardinagem', 'Resíduos de poda',
    'Resíduos de folhas', 'Resíduos de galhos', 'Resíduos de troncos', 'Resíduos de terra',
    'Resíduos de areia', 'Resíduos de pedras', 'Resíduos de concreto', 'Resíduos de asfalto'
]
             
    palavra = entrada.get().capitalize()
    if palavra in lista:
        txt.delete('1.0', END)
        txt.insert(END, f'O Objeto {palavra} é Descartável/Reciclavél!\nVerifique de lavar bem este objeto antes de descarta-lo.\nObrigado!')
    elif entrada.get() == '':
        txt.delete('1.0', END)
        txt.insert(END, f'Voce precisa inserir um item para o sistema verificar !')
    else:
        txt.delete('1.0', END)
        txt.insert(END, f'O Objeto {palavra} Não é reciclável.\nLembre-se de Verificar o melhor local para o seu Descarte!.\nCaso houver duvidas, entre em contato com o administrador.')
def open_file():
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
janu.geometry('520x250')
janu.iconbitmap('')
janu.resizable(False, False)
janu.configure(background='black')

cred = Button(janu, text='P.K0m', bg='#07F7FB', fg='#000', font=('Arial', 11))
cred.place(x=380, y=32)

cred2 = Button(janu, text='G. Blasio', bg='#C707FB', fg='#000', font=('Arial', 11))
cred2.place(x=290, y=32)

sair_botao = Button(janu, text='Sair', bg='red', fg='white', font=('Arial', 12), command=janu.quit)
sair_botao.place(x=115, y=32)

saiba_mais = Button(janu, text='Saiba mais!', bg='brown', fg='white', font=('Arial', 12), command=open_file)
saiba_mais.place(x=5, y=32)

executar = Button(janu, text='go', bg='#3FFA22', fg='#000', font=('Arial', 12), command=reciclaveis)
executar.place(x=467, y=6)

entrada = Entry(janu, bg='white', fg='black', width=45, font=('Arial', 13))
entrada.place(x=5, y=5)

ajuda = Label(janu, text='Descubra a melhor maneira de descartar seu Lixo!', fg='#FFF', bg='#2604FF', font=('Arial', 14), width=60)
ajuda.pack(pady=70)

txt = Text(janu, background='pink', height=5, font=('Arial', 14), fg='Black')
txt.place(x=1, y=100)

frase = Label(janu, text='Um pequeno gesto, um grande impacto: recicle!', fg='#FFF', bg='#197d05', font=('Arial', 12), width=60)
frase.pack(pady=25)


horario_label = Label(janu, text='', font=('Arial', 18))
horario_label.place(x=190,y=32)

mostrar_horario()

janu.mainloop()
