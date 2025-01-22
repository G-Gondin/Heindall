import script, os, time
if script.arqexiste("usersh.csv") == False:
    script.criararq("usersh.tcsv")

while True:
    print("""[1] Entrar
[2] Criar
[3] Sair""")
    choice = str(input("Qual sua escolha? ")).strip()
    if len(choice) > 1:
        print("Escolha apenas uma opção")
        time.sleep(1.5)
        os.system("cls")
        continue
    elif choice == "" or choice not in "123":
        print("Erro, tente novamente")
        time.sleep(1.5)
        os.system("cls")
        continue
    
    if choice == "1":
        while True:
            log_user = str(input("Digite o nome de usuario: ")).strip()
            if script.verify_loguser(log_user) == False:
                print("Usuario não encontrado")
                choise = str(input("[1] Tentar novamente ou [2] sair? ")).strip()
                if len(choise) > 1 or choise not in "12" or choise == "":
                    while len(choise) > 1 or choise not in "12" or choise == "":
                        choise = str(input("Opção invalida, tente novamente: ")).strip()
                if choise == "1":
                    time.sleep(1.5)
                    os.system("cls")
                    continue
                elif choise == "2":
                    choise = ""
                    break
            while True:
                log_pass = str(input("Digite a Senha: ")).strip()
                if script.verify_logpass(log_pass) == False:
                    print("Senha incorreta!")
                    choise = str(input("[1] Tentar novamente ou [2] sair? ")).strip()
                    if len(choise) > 1 or choise not in "12" or choise == "":
                        while len(choise) > 1 or choise not in "12" or choise == "":
                            choise = str(input("Opção invalida, tente novamente: ")).strip()
                    if choise == "1":
                        time.sleep(1.5)
                        os.system("cls")
                        continue
                    elif choise == "2":
                        choise = ""
                        c = 1
                        break
                print("Login realizado com sucesso.")
                c = 1
                break
            if c == 1:
                c = 0
                break

    elif choice == "2":
        while True:
            user_name = str(input("Digite seu nome: ")).strip().lower()
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
        script.cadastro("usersh.csv", user_name, user_pass)
        time.sleep(1.5)
        os.system("cls")

    elif choice == "3":    
        time.sleep(1.5)
        os.system("cls")
        break
time.sleep(1)
print("Tenha um bom dia, tarde ou noie")
