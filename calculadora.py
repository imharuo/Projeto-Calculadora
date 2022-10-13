from tkinter import *
from tkinter import ttk

# colors
black_color: str = '#050505'
grey_color: str = '#242424'
greyblack_color: str = '#1a1a1a'
white_color: str = '#fcf7f7'

# config janela
janela: ttk = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.configure(bg = black_color)
janela.resizable(width=False, height=False)

# frames
frame1 = Frame(janela, width=235, height=50, bg=grey_color)
frame1.grid(row=0, column=0)

frame2 = Frame(janela, width=235, height=268 )
frame2.grid(row=1, column=0)

# variavel para guardar valores digitados
todos_valores = ''

# variavel valor texto
valor_texto = StringVar()

# funcao para aparecer os valores digitados
def entrada_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    # passando valor para o botao
    valor_texto.set(todos_valores)

# funcao para calcular
def calcula():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


# funcao clear(limpa tela)
def clear():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

# labels
app_label = Label(frame1, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor=E, justify=RIGHT, font= 'Arial 18', bg=grey_color, fg=white_color)
app_label.place(x=0, y=0)

# botoes
b1 = Button(frame2, command = lambda: entrada_valores('%'), text='%', width=7, height=3, bg=greyblack_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame2, command = lambda: entrada_valores('/'), text='/', width=7, height=3, bg=greyblack_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b2.place(x=59, y=0)
b3 = Button(frame2, command = clear, text='C', width=16, height=3, bg=greyblack_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b3.place(x=118, y=0)

b4 = Button(frame2, command = lambda: entrada_valores('7'), text='7', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frame2, command = lambda: entrada_valores('8'), text='8', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(frame2, command = lambda: entrada_valores('9'), text='9', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(frame2, command = lambda: entrada_valores('*'), text='x', width=7, height=3, bg=greyblack_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)

b8 = Button(frame2, command = lambda: entrada_valores('4'), text='4', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=105)
b9 = Button(frame2, command = lambda: entrada_valores('5'), text='5', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=105)
b10 = Button(frame2, command = lambda: entrada_valores('6'), text='6', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=105)
b11 = Button(frame2, command = lambda: entrada_valores('-'), text='-', width=7, height=3, bg=greyblack_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=105)

b12 = Button(frame2, command = lambda: entrada_valores('1'), text='1', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=159)
b13 = Button(frame2, command = lambda: entrada_valores('2'), text='2', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=159)
b14 = Button(frame2, command = lambda: entrada_valores('3'), text='3', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=159)
b15 = Button(frame2, command = lambda: entrada_valores('+'), text='+', width=7, height=3, bg=greyblack_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=159)

b16 = Button(frame2, command = lambda: entrada_valores('0'), text='0', width=16, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=214)
b17 = Button(frame2, command = lambda: entrada_valores('.'), text='.', width=7, height=3, bg=black_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=214)
b18 = Button(frame2, command = calcula, text='=', width=7, height=3, bg=greyblack_color, fg=white_color, relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=214)


janela.mainloop()