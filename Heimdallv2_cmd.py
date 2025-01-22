import os, time, script
from script import limpa
if script.arqexiste("usersh.csv") == False:
    script.criararq("usersh.csv")

if script.arqexiste("produtos.csv") == False:
    script.criararq("produtos.csv")

sys = """[1] Produtos
[2] Usuarios
[3] Logout"""

produt = """[1] Cadastrar novo produto
[2] Verificar produtos
[3] Voltar"""

usua = """[1] Editar suas informações
[2] Editar informações de 3°
[3] Criar novo usuario
[4] Ver usuarios
[5] Voltar"""

log = 0
while True:
    if log != 1:
        log_user = str(input("Usuario: ")).strip()
        if script.verify_loguser(log_user) == False:
            print("Usuario não enctrado ou incorreto.")
            limpa()
            continue
        else:
            while True:
                log_info = script.coletainfo_un(log_user)
                log_pass = str(input("Senha: ")).strip()
                if log_pass != log_info[1]:
                    print("Senha incorreta.")
                    limpa()
                    continue
                else:
                    log = 1
                    print("login realizado com sucesso")
                    time.sleep(0.5)
                    print("...")
                    break
    limpa()
    print(sys)
    choice = str(input("Qual sua escolha? ")).strip()
    if len(choice) > 1 or choice == "" or choice not in "123":
        while len(choice) > 1 or choice == "" or choice not in "123":
            choice = str(input("Erro, escolha novamente: "))
    if choice == "1":
        limpa()
        while True:
            print(produt)
            choice1 = str(input("Qual sua escolha? ")).strip()
            if len(choice1) > 1 or choice1 == "" or choice1 not in "123":
                while len(choice1) > 1 or choice1 == "" or choice1 not in "123":
                    choice1 = str(input("Erro, escolha novamente: "))
            if choice1 == "1":
                limpa()
                crcd = str(input("Deseja que seja criado um novo código de produto? [s/n] ")).strip().lower()
                if len(crcd) > 1 or crcd == "" or crcd not in "sn":
                    while len(crcd) > 1 or crcd == "" or crcd not in "sn":
                        crcd = str(input("Erro, digite novamente: ")).strip().lower()
                if crcd == "s":
                    codi = script.criacod()
                    print(f"Seu novo código é: {codi}")
                if crcd == "n":
                    codi = str(input("Digite o seu código: ")).strip()
                    print(codi)
                    if len(codi) != 12 or codi == "":
                        while len(codi) != 12 or codi == "":
                            codi = str(input("Erro, digite seu código novamente: ")).strip()
                nome = str(input("Digite o nome do produto: ")).strip().capitalize()
                if nome == "" or script.autentic_name(nome) == False:
                    while nome == "" or script.autentic_name(nome) == False:
                        nome = str(input("Erro, escreva novamente: "))
                pr = str(input("Deseja adicionar preço? [s/n] ")).strip().lower()
                if len(pr) > 1 or pr == "" or pr not in "sn":
                    while len(pr) > 1 or pr == "" or pr not in "sn":
                        pr = str(input("Erro, digite novamente, [S] sim ou [N] não? ")).strip().lower()
                if pr == "s":
                    while True:
                        try:
                            price = int(input("Qual o valor do item: "))
                        except:
                            continue
                        else:
                            print(script.cadastro_prod("produtos.csv", codi, nome, price))
                            break
                if pr == "n":
                    print(script.cadastro_prod("produtos.csv", codi, nome))
            if choice1 == "2":
                limpa()
                script.lercadat_prod("produtos.csv")
                edit = str(input("Deseja editar algum produto? [S/N]")).strip().upper()
                if edit not in "SN" or edit == "" or len(edit) > 1:
                    while edit not in "SN" or edit == "" or len(edit) > 1:
                        edit = str(input("Erro! Digite novamente: ")).strip().upper()
                if edit == "S":
                    op = str(input("Digite o código do produto que você quer editar: "))
                    script.alt_val_prod("produtos.csv", op)
            if choice1 == "3":
                break
            limpa()
    if choice == "2":
        while True:
            limpa()
            print(usua)
            ch2 = str(input("Qual sua escolha? ")).strip()
            if len(ch2) > 1 or ch2 == "" or ch2 not in "12345":
                while len(ch2) > 1 or ch2 == "" or ch2 not in "12345":
                    ch2 = str(input("Erro, escolha novamente: "))
            if ch2 == "1":
                n1 = str(input("""[1] Nome
[2] Senha
[3] Voltar
O que você quer alterar? """)).strip()
                if n1 not in "123" or n1 == "" or len(n1) > 1:
                    while n1 not in "123" or n1 == "" or len(n1) > 1:
                        n1 = str(input("Erro, digite novamente: ")).strip()
            if ch2 == "2":
                if log_info[3] == "nao":
                    print("Você não tem permissão para acessar essa parte")
                else:
                    while True:
                        limpa()
                        find_log = str(input("Digite o nome ou id do usuario que deseja alterar: ")).strip().lower()
                        if script.verify_unamein(find_log) == False and script.verify_uidin(find_log) == False:
                            logu = str(input("Usuario não encontrado, [S] sair ou [T] tentar novamente? ")).strip().lower()
                            if logu == "" or logu not in "st" or len(logu) > 1:
                                while logu == "" or logu not in "st" or len(logu) > 1:
                                    logu = str(input("Erro, tente de novo: ")).strip().lower()
                            if logu == "s":
                                break
                            if logu == "t":
                                continue
                        else:
                            script.alt_cad_user("usersh.csv", find_log)
                            break
            if ch2 == "3":
                while True:
                    user_name = str(input("Digite o nome: ")).strip().lower()
                    if script.verify_name(user_name) == False:
                        print("Nome invalido, já cadastrado ou com letras em sequencia, tente novamente.")
                        time.sleep(1.5)
                        os.system("cls")
                        continue
                    else:
                        break
                while True:
                    user_pass = str(input("Digite sua senha: ")).strip()
                    if script.verify_pass(user_pass) == False:
                        print("Senha invalida, não pode numeros em sequencia, tem que ser maior que 4 e menor que 8, tente novamente.")
                        time.sleep(1.5)
                        os.system("cls")
                        continue
                    else:
                        break
                script.cadastra_users("usersh.csv", user_name, user_pass)
            if ch2 == "4":
                script.lercadat_users("usersh.csv")
                n1 = input("Pressione Enter para sair ")
            if ch2 == "5":
                break
    if choice == "3":
        print("Fazendo logout, aguarde...")
        log = 0
        limpa()
        break
print("Volte sempre")
time.sleep(1)
