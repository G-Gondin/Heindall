import customtkinter as ctk
import sys

def arqexiste(nome):
    try:
        with open(nome, "rt") as a:
            pass
    except FileNotFoundError:
        return False
    return True

def criararq(nome):
    with open(nome, "wt+") as a:
        pass

def coletainfo_un(name):
    """Retorna todas as informações cadastrais de determinado usuário"""
    with open("usersh.csv", "rt") as a:
        for c in a:
            dado = c.strip().split(",")
            if dado[0] == name:
                return dado
    return None

def verify_loguser(user):
    """Verifica ou encontra um usuário que está ou não presente na lista"""
    with open("usersh.csv", "rt") as a:
        for c in a:
            dado = c.strip().split(",")
            if dado[0] == user:
                return True
    return False

class LoginApp:
    def __init__(self):
        self.login_sucesso = False

    def tela_login(self):
        """Função para exibir a tela de login e verificar credenciais."""

        def verificar_login():
            user = entry_usuario.get()
            senha = entry_senha.get()

            if not verify_loguser(user):
                label_erro.configure(text="Usuário não encontrado!", text_color="red")
                label_erro.place(x=105, y=85)
            else:
                dados = coletainfo_un(user)
                if dados and senha == dados[1]:
                    self.login_sucesso = True
                    janela_login.destroy()  # Fecha a janela de login
                else:
                    label_erro.configure(text="Senha incorreta!", text_color="red")
                    label_erro.place(x=125, y=85)

        janela_login = ctk.CTk()
        ctk.set_appearance_mode("Light")
        janela_login.geometry("252x125")
        janela_login.title("Heimdall")
        janela_login.resizable(False, False)  # Impede redimensionamento da janela
        janela_login.iconbitmap("grego.ico")

        # Label do campo de usuário
        label_usuario = ctk.CTkLabel(janela_login, text="Login: ")
        label_usuario.place(x=10, y=15)

        # Entrada do campo de usuário
        entry_usuario = ctk.CTkEntry(janela_login, width=185)
        entry_usuario.place(x=60, y=15)

        # Label do campo de senha
        label_senha = ctk.CTkLabel(janela_login, text="Senha: ")
        label_senha.place(x=8, y=50)

        # Entrada do campo de senha (com máscara)
        entry_senha = ctk.CTkEntry(janela_login, show="*", width=185)
        entry_senha.place(x=60, y=50)

        # Label de erro (inicialmente vazio)
        label_erro = ctk.CTkLabel(janela_login, text="")
        label_erro.place(x=105, y=85)

        # Botão de login
        botao_login = ctk.CTkButton(janela_login, text="Login", fg_color="blue", command=verificar_login, width=90)
        botao_login.place(x=5, y=85)

        # Iniciar a janela de login
        janela_login.mainloop()

if not arqexiste("usersh.csv"):
    criararq("usersh.csv")

# Inicializa o login
login_app = LoginApp()
login_app.tela_login()

# Verifica se o login foi concluído com sucesso
if not login_app.login_sucesso:
    sys.exit("Login obrigatório. Encerrando o programa.")

# Configuração da janela principal
janela_principal = ctk.CTk()
janela_principal.geometry("600x450")
janela_principal.title("Heimdall")
janela_principal.iconbitmap("grego.ico")
ctk.set_appearance_mode("Light")

label_bemvindo = ctk.CTkLabel(janela_principal, text="Bem-vindo(a) à Janela Principal!", font=("Arial", 16))
label_bemvindo.pack(pady=20)

janela_principal.mainloop()
