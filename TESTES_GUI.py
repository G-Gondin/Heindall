import customtkinter as ctk
from PIL import Image, ImageTk

# Inicializar o tema do customtkinter
ctk.set_appearance_mode("light")  # Modos: "System" (padrão), "Light", "Dark"
ctk.set_default_color_theme("blue")  # Temas: "blue", "dark-blue", "green"

# Criar a janela principal
root = ctk.CTk()
root.geometry("400x300")
root.title("Botão com Imagem")

# Carregar a imagem
image = Image.open("grego.png")  # Substitua pelo caminho correto
image_resized = image.resize((40, 40))  # Redimensionar a imagem
image_ctk = ImageTk.PhotoImage(image_resized)

# Função para ser chamada ao clicar no botão
def on_button_click():
    print("Botão clicado!")

# Criar o botão
button = ctk.CTkButton(
    root,
    text="",  # Deixe vazio para exibir apenas a imagem
    image=image_ctk,
    width=100,
    height=50,
    corner_radius=10,  # Para bordas arredondadas
    fg_color="transparent",  # Fundo transparente
    hover_color="lightgray",  # Cor ao passar o mouse
    command=on_button_click,
)
button.pack(pady=50)

# Rodar o loop principal
root.mainloop()
