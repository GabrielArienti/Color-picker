from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Cores
branco = "#fcfcfc"
branco_claro = "#f2f2f2"
preto = "#030303"
preto_cinza = "#1f1d1d"
azul = "#04007d"
amarelo = "#edfa00"
laranja = "#fa9200"
vermelho = "#8c0601"
verde = "#0f8c01"


janela = Tk()
janela.title("Color Picker")
janela.config(bg=branco)
janela.geometry("530x200")
janela.resizable(width=FALSE, height=FALSE)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Tela mostradora

tela = Label(janela, bg=preto, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg=branco)
frame_direita.grid(row=0, column=2, padx=5, pady=5)

frame_baixo = Frame(janela, bg=branco)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)


# Função escala e copiar

def escala(valor):
    red = scale_red.get()
    green = scale_green.get()
    blue = scale_blue.get()

    # variável que une valores acima
    rgb = f'{red}, {green}, {blue}'
    hexadecimal = "#%02x%02x%02x" % (red, green, blue)

    tela['bg'] = hexadecimal
    entry_codigo.delete(0, END)
    entry_codigo.insert(0, hexadecimal)


def copiar():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(entry_codigo.get())
    clip.destroy()
    messagebox.showinfo("Copiar", "Código copiado!")


# Configurando frame direita e escalas de cores


# ---------- Escala vermelho
label_red = Label(frame_direita, text="Red", width=7,
                  font="Raleway 12 bold", bg=branco, fg=vermelho, anchor=NW)
label_red.grid(row=0, column=0)

scale_red = Scale(frame_direita, command=escala, from_=0, to=255,
                  length=150, bg=branco, fg=vermelho, orient=HORIZONTAL)
scale_red.grid(row=0, column=1)

# ---------- Escala verde
label_green = Label(frame_direita, text="Green", width=7,
                    font="Raleway 12 bold", bg=branco, fg=verde, anchor=NW)
label_green.grid(row=1, column=0)

scale_green = Scale(frame_direita, command=escala, from_=0, to=255,
                    length=150, bg=branco, fg=verde, orient=HORIZONTAL)
scale_green.grid(row=1, column=1)


# ---------- Escala Azul
label_blue = Label(frame_direita, text="Blue", width=7,
                   font="Raleway 12 bold", bg=branco, fg=azul, anchor=NW)
label_blue.grid(row=2, column=0)

scale_blue = Scale(frame_direita, command=escala, from_=0, to=255,
                   length=150, bg=branco, fg=azul, orient=HORIZONTAL)
scale_blue.grid(row=2, column=1)


# Configurando Frame Baixo

label_rgb = Label(frame_baixo, text="CÓDIGO",
                  font="Raleway 10 bold", bg=branco, fg=preto, anchor=NW)
label_rgb.grid(row=0, column=0, padx=5)

entry_codigo = Entry(frame_baixo, text="", width=12,
                     font="Raleway 10", justify=CENTER)
entry_codigo.grid(row=0, column=1, padx=5)

botao = Button(frame_baixo, command=copiar,
               text="Copiar", font="Raleway 10 bold", )
botao.grid(row=0, column=2, padx=5)


janela.mainloop()
