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