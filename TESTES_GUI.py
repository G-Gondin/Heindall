import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk


ctk.set_appearance_mode("light")  # Modos: "System" (padrão), "Light", "Dark"
# Criar a janela principal
janela_principal = ctk.CTk()
janela_principal.geometry("600x450")
janela_principal.title("Botão com Imagem")

# Criar um frame que ocupa toda a janela
frame_fundo = ctk.CTkFrame(
    janela_principal,
    width=600,
    height=450,
    fg_color="#f7f7f7",)  # Cor de fundo da janela (hexadecimal)
frame_fundo.pack(fill="both", expand=True)  # Preencher a janela com o frame

# Adicionar a barra vertical
barra_vertical = ctk.CTkFrame(
    janela_principal,
    width=35,  # Largura da barra
    height=450,  # Altura da barra
    fg_color="#dedede",  # Cor da barra (hexadecimal)
    corner_radius=0,) # Barra quadrada
barra_vertical.place(x=0, y=0)  # Posiciona no canto superior esquerdo da janela


#variaveis de controle
interface_options = False
options = None
interface_itens = False
itens = None

#def para fechar todas as janelas
def closall():
    global interface_options, options, interface_itens, itens

    if interface_options and options:
        options.destroy()
        options = None
        interface_options = False
    
    if interface_itens and itens:
        itens.destroy()
        itens = None
        interface_itens = False


#Botão eu 
# Carregar a imagem
imgop = Image.open("Imagens\options.png")  # Substitua pelo caminho correto
imageop_resized = imgop.resize((30, 20))  # Redimensionar a imagem
imageop_ctk = ImageTk.PhotoImage(imageop_resized)
# Função para ser chamada ao clicar no botão
def boptions():
    global options, interface_options  
    if interface_options:
        closall()
    else:
        closall()
        options = ctk.CTkFrame(janela_principal, width=171, height=50, corner_radius=0, fg_color="#dedede")
        options.place(x=34, y=0)
        interface_options = True
# Criar o botão
buttonop = ctk.CTkButton(
    janela_principal,
    text="",  # Deixe vazio para exibir apenas a imagem
    image=imageop_ctk,
    width=30,
    height=20,
    corner_radius=0,  # Para bordas arredondadas
    fg_color="#dedede",  # Fundo transparente
    hover_color="lightgray",  # Cor ao passar o mouse
    command=boptions,)
buttonop.place(x=0, y=0)





#Botão itens
# Carregar a imagem
imageit = Image.open("Imagens\Box.png")  # Substitua pelo caminho correto
imageit_resized = imageit.resize((30, 25))  # Redimensionar a imagem
imageit_ctk = ImageTk.PhotoImage(imageit_resized)
# Função para ser chamada ao clicar no botão
def bitens():
    global itens, interface_itens  
    if interface_itens:
        closall()
    else:
        closall()
        itens = ctk.CTkFrame(janela_principal, width=35, height=90, corner_radius=0, fg_color="#dedede")
        itens.place(x=34, y=160)
        interface_itens = True
# Criar o botão
buttonit = ctk.CTkButton(
    janela_principal,
    text="",  # Deixe vazio para exibir apenas a imagem
    image=imageit_ctk,
    width=30,
    height=25,
    corner_radius=0,  # Para bordas arredondadas
    fg_color="#dedede",  # Fundo transparente
    hover_color="lightgray",  # Cor ao passar o mouse
    command=bitens)
buttonit.place(x=0, y=190)





#Botão pessoas
# Carregar a imagem
image = Image.open("Imagens\person.png")  # Substitua pelo caminho correto
image_resized = image.resize((30, 30))  # Redimensionar a imagem
image_ctk = ImageTk.PhotoImage(image_resized)
# Função para ser chamada ao clicar no botão
def on_button_click():
    print("bitão apertado")
# Criar o botão
button = ctk.CTkButton(
    janela_principal,
    text="",  # Deixe vazio para exibir apenas a imagem
    image=image_ctk,
    width=35,
    height=35,
    corner_radius=0,  # Para bordas arredondadas
    fg_color="#dedede",  # Fundo transparente
    hover_color="lightgray",  # Cor ao passar o mouse
    command=on_button_click,)
button.place(x=0, y=225)





#Botão sair
# Carregar a imagem
image = Image.open("Imagens\onoff.png")  # Substitua pelo caminho correto
image_resized = image.resize((30, 30))  # Redimensionar a imagem
image_ctk = ImageTk.PhotoImage(image_resized)
# Função para ser chamada ao clicar no botão
def dext():
    global jansa  # Para evitar múltiplas instâncias

    # Criar uma subjanela (janela filha) corretamente
    jansa = ctk.CTkToplevel(janela_principal)
    jansa.geometry("180x85")
    jansa.title("Confirmação de Saída")

    # Definir como janela modal
    jansa.transient(janela_principal)  # Define como filha da janela principal
    jansa.grab_set()  # Bloqueia interações com a janela principal

    def dexs():
        jansa.destroy()
        janela_principal.destroy()

    def dexn():
        jansa.destroy()

    # Impedir fechamento no "X" sem resposta do usuário
    jansa.protocol("WM_DELETE_WINDOW", dexn)

    label_saida = ctk.CTkLabel(jansa, text="Tem certeza que deseja\n encerrar o programa?")
    label_saida.place(x=25, y=5)

    btss = tk.Button(
        jansa,
        relief="raised",
        borderwidth=5,
        text="Sim",
        font=("", 8),
        width=5,
        height=0,
        command=dexs)
    btss.place(x=40, y=47)

    btsn = tk.Button(
        jansa,
        relief="raised",
        borderwidth=5,
        text="Não",
        font=("", 8),
        width=5,
        height=0,
        command=dexn)
    btsn.place(x=110, y=47)


# Criar o botão
button = ctk.CTkButton(
    janela_principal,
    text="",  # Deixe vazio para exibir apenas a imagem
    image=image_ctk,
    width=30,
    height=30,
    corner_radius=0,  # Para bordas arredondadas
    fg_color="#dedede",  # Fundo transparente
    hover_color="lightgray",  # Cor ao passar o mouse
    command=dext,)
button.place(x=0, y=417)















# Rodar o loop principal
janela_principal.mainloop()
