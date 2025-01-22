def limpa():
    """limpa tudo"""
    import time, os
    time.sleep(1.5)
    os.system("cls")

def arqexiste(nome):
    try:
        a = open(nome, "rt")
    except FileNotFoundError:
        return False
    else:
        return True

def criararq(nome):
    a = open(nome, "wt+")
    a.close()

def cria_id():
    """Cria um ID aleatoriamente"""

    from random import randint
    id = ""
    while len(id) < 7:
        id += str(randint(1, 9))
    return id
        
def verify_id(arq, id):
    """Verifica se tem um determinado id dentro do arquivo selecionado
    arq = arquivo selecionado
    id = id a ser verificado"""
    
    n1 = open(arq, "rt")
    for c in n1:
        lis = c.split(",")
        if lis[2] == id:
            n1.close()
            return True
    else:
        n1.close()
        return False

def cadastra_users(arq, name, upass, id="cria", permis="nao"):
    """Realiza a adição de um novo usuario no arquivo desejado
    arq = arquivo desejado
    name = nome de usuario
    upass = senha do usuario
    permis = se não selecionada como sim, como padrão sem autorização"""
    
    if id == "cria":
        while True:
            ids = cria_id()
            vid = verify_id(arq, ids)
            if vid == True:
                continue
            else:
                break
    else:
        try:
            a = open(arq, "at")
            a.write(f"{name},{upass},{id},{permis}")
            a.close()
        except:
            return "Houve um erro inesperado"
        else:
            return "Pessoa cadastrada com sucesso!"
    
def verify_uidin(id):
    """Verifica se determinado ID já está presente no arquivo local"""
    
    n1 = open("usersh.csv", "rt")
    for c in n1:
        lis = c.split(",")
        if lis[2] == id:
            n1.close()
            return True
    else:
        n1.close()
        return False

def verify_unamein(name):
    """Verifica se determinado nome já está presente no arquivo local"""
    
    n1 = open("usersh.csv", "rt")
    for c in n1:
        lis = c.split(",")
        if lis[0] == name:
            n1.close()
            return True
    else:
        n1.close()
        return False

def verify_sqt(name):
    """Verifica se o nome tem letras em sequencia"""
    
    alfab = "abcdefghijklmnopqrstuvwxyz"
    nm = name
    l = []
    for c in range(0, len(nm)):
        l.append(nm[c])
    for c in range(0, len(l)):
        p = alfab.find(l[c])
        try: 
            if l[c+1] == alfab[p+1]:
                return False
        except:
            return True

def verify_name(name):
    """Verifica se um determinado nome está em ordem para ser usado"""
    
    if verify_unamein(name) == True:
        return False
    if verify_sqt(name) == False:
        return False
    else:
        return True

def verify_pass(upass):
    """verifica se uma determinada senha está apropriada para uso"""

    if 5 > len(upass) or len(upass) > 7:
        return False
    nums = "0123456789"
    nm = upass
    l = []
    for c in range(0, len(nm)):
        l.append(nm[c])
    for c in range(0, len(l)):
        p = nums.find(l[c])
        try: 
            if l[c+1] == nums[p+1]:
                return False
        except:
            return True
        
def verify_loguser(user):
    """verifica ou encontra um usuario que está ou não presente na lista"""
    
    a = open("usersh.csv", "rt")
    clients = []
    for c in a:
        clients.append(c.split(","))
        if clients[0][0] == user:
            return True
        else:
            clients.clear()
    a.close()
    return False

def criacod():
    from random import randint
    cod = "782147"
    ultimo_dig = 0
    for c in range(0, 5):
        num = randint(0, 9)
        cod += str(num)
        ultimo_dig += num
    if ultimo_dig > 10:
        while ultimo_dig >= 10:
            ultimo_dig -= 10
    cod += str(ultimo_dig)
    return cod

def autentic_name(name):
    alfab = "abcdefghijklmnopqrstuvwxyz"
    t = ""
    nm = name
    l = []
    for c in range(0, len(nm)):
        l.append(nm[c])
    for c in range(0, len(l)):
        if l[c].lower() in alfab:
            t += l[c]
    if len(t) < 3:
        return False
    else:
        return True
    
def cadastro_prod(arq, cod, name, preco=0):
    from datetime import date
    try:
        data = date.today()
        a = open(arq, "at")
        a.write(f"{cod},{name},{preco},{data}")
        a.write("\n")
        a.close()
    except:
        return "Houve um erro inesperado"
    else:
        return "Produto cadastrado com sucesso!"

def lercadat_prod(arq):
    def linha1():
        print("-" * 57)

    a = open(arq, "rt")
    linha1()
    for c in a:
        dado = c.split(",")
        print(f"{f"{dado[0]} {dado[1]}":<25}\t {f"R$ {dado[2]} Data: {dado[3]}":>2}")
    linha1()
    a.close()

def verify_pcodin(arq, ver):
    n1 = open(arq, "rt")
    for c in n1:
        lis = c.split(",")
        if lis[0] == ver:
            n1.close()
            return True
    else:
        n1.close()
        return False

def verify_pnamein(arq, ver):
    n1 = open(arq, "rt")
    for c in n1:
        lis = c.split(",")
        if lis[1] == ver:
            n1.close()
            return True
    else:
        n1.close()
        return False

def alt_val_prod(arq, cod):
    if verify_pcodin(arq, cod) == False:
        return print("Produto não encontrado")
    else:
        a = open(arq, "rt")
        produtos = []
        for c in a:
            produtos.append(c.split(","))
        a.close()
        lis = []
        for c in range(0, len(produtos)):
            if produtos[c][0] == cod:
                lis = produtos[c].copy()
        produtos.remove(lis)
        
        choice = str(input("Você deseja alterar um valor ou remove-lo? [A/R] ")).strip().lower()
        if choice not in "ar" or choice == "" or len(choice) > 1:
            while choice not in "ar" or choice == "" or len(choice) > 1:
                choice = str(input("Erro, digite novamente: ")).strip().lower()
        
        if choice == "a":
            n1 = str(input("""[1] código
[2] Nome
[3] Preço
Qual dado você quer alterar? """)).strip()
            if n1 not in "123" or n1 == "" or len(n1) > 1:
                while n1 not in "123" or n1 == "" or len(n1) > 1:
                    n1 = str(input("Erro! Digite novamente: ")).strip()
            if n1 == "1":
                while True:
                    new = str(input("Digite o novo código: "))
                    if verify_pcodin(arq, new) == True:
                        continue
                    else:
                        lis[0] = new
                        break
            if n1 == "2":
                while True:
                    new = str(input("Digite o novo nome: "))
                    if verify_pnamein(arq, new) == True:
                        continue
                    else:
                        lis[1] = new
                        break
            if n1 == "3":
                while True:
                    try:
                        new = int(input("Digite o novo preço: "))
                        lis[2] = new
                    except:
                        continue
                    else:
                        break
            produtos.append(lis)
            a = open(arq, "wt")
            for c in range(0, len(produtos)):
                cadastro_prod(arq, produtos[c][0], produtos[c][1], produtos[c][2])
            a.close
            return print("Alteração realizada com sucesso.")

        if choice == "r":
            a = open(arq, "wt")
            for c in range(0, len(produtos)):
                cadastro_prod(arq, produtos[c][0], produtos[c][1], produtos[c][2])
            a.close()
            return print("Produto removido com sucesso!")

def lercadat_users(arq):
    def linha1():
        print("-" * 85)

    a = open(arq, "rt")
    linha1()
    for c in a:
        dado = c.split(",")
        print(f"""
user name: {dado[0]} | senha: {dado[1]} | id: {dado[2]} | permissão de alteração: {dado[3]}
""")
    linha1()
    a.close()

def coletainfo_uid(id):
    """retorna todas as informações cadastrais de determinado usuario"""

    a = open("usersh.csv", "rt")
    for c in a:
        dado = c.split(",")
        if dado[2] == id:
            return dado
    else:
        a.close()
        return "Algo deu errado!"

def coletainfo_un(name):
    """retorna todas as informações cadastrais de determinado usuario"""

    a = open("usersh.csv", "rt")
    for c in a:
        dado = c.split(",")
        if dado[0] == name:
            return dado
    else:
        a.close()
        return "Algo deu errado!"

def alt_cad_user(arq, cod):
    #descobro se é nome ou id
    if verify_uidin(cod) == False:
        busca = "nome"
    if verify_unamein(cod) == False:
        busca = "id"
    #busco por nome ou id
    if busca == "id":
        if verify_uidin(cod) == False:
            return "Usuario não encontrado"
    if busca == "nome":
        if verify_unamein(cod) == False:
            return "Usuario não encontrado"
    
    #jogando todos os usuarios para lista
    a = open(arq, "rt")
    tusuarios = []
    for c in a:
        tusuarios.append(c.split(","))
    a.close()


    #coletando as informações pelo nome
    if busca == "nome":
        lis = []
        for c in range(0, len(tusuarios)):
            if tusuarios[c][0] == cod:
                lis = tusuarios[c].copy()
        tusuarios.remove(lis)
    #coletando as informações por id
    if busca == "id":
        lis = []
        for c in range(0, len(tusuarios)):
            if tusuarios[c][2] == cod:
                lis = tusuarios[c].copy()
        tusuarios.remove(lis)
    #alterar ou remover
    choice = str(input("Você deseja alterar um valor ou remove-lo? [A/R] ")).strip().lower()
    if choice not in "ar" or choice == "" or len(choice) > 1:
        while choice not in "ar" or choice == "" or len(choice) > 1:
            choice = str(input("Erro, digite novamente: ")).strip().lower()
    
    
    #alterar
    if choice == "a":
        n1 = str(input("""[1] Nome
[2] Senha
[3] Permissão
Qual dado você quer alterar? """)).strip()
        if n1 not in "123" or n1 == "" or len(n1) > 1:
            while n1 not in "123" or n1 == "" or len(n1) > 1:
                n1 = str(input("Erro! Digite novamente: ")).strip()
        if n1 == "1":
            while True:
                    user_name = str(input("Digite seu nome: ")).strip().lower()
                    if verify_name(user_name) == False:
                        print("Nome invalido, já cadastrado ou com letras em sequencia, tente novamente.")
                        limpa()
                        continue
                    else:
                        lis[0] = user_name
                        break
        elif n1 == "2":
            while True:
                    user_pass = str(input("Digite sua senha: ")).strip()
                    if verify_pass(user_pass) == False:
                        print("Senha invalida, não pode numeros em sequencia, tem que ser maior que 4 e menor que 8, tente novamente.")
                        limpa()
                        continue
                    else:
                        lis[1] = user_pass
                        break
        elif n1 == "3":
            if lis[3] == "nao":
                bah = str(input(f"O usuario não tem permissão para realizar certas ações, conceder acesso? [S/N]")).strip().lower()
                if bah not in "sn" or bah == "" or len(bah) > 1:
                    while bah not in "sn" or bah == "" or len(bah) > 1:
                        bah = str(input("Erro, digite novamente: ")).strip().lower()
                if bah == "s":
                    lis[3] = "sim"
            elif lis[3] == "sim":
                bah = str(input(f"O usuario tem permissão para realizar certas ações, retirar o acesso? [S/N]")).strip().lower()
                if bah not in "sn" or bah == "" or len(bah) > 1:
                    while bah not in "sn" or bah == "" or len(bah) > 1:
                        bah = str(input("Erro, digite novamente: ")).strip().lower()
                if bah == "s":
                    lis[3] = "nao"
        
        tusuarios.append(lis)        
        a = open(arq, "wt")
        for c in range(0, len(tusuarios)):
            cadastra_users("usersh.csv", tusuarios[c][0], tusuarios[c][1], tusuarios[c][2], tusuarios[c][3])
        return "Alteração realizada com sucesso."
    #remover
    if choice == "r":
        a = open(arq, "wt")
        for c in range(0, len(tusuarios)):
            cadastra_users(arq, tusuarios[c][0], tusuarios[c][1], tusuarios[c][2], tusuarios[c][3])
        a.close()
        return "Produto removido com sucesso!"
    
def valida_codi(codi):
    if codi == "":
        return False
    elif len(codi) != 12:
        return False
    elif verify_pcodin("produtos.csv", codi) == True:
        print("Código já utilizado")
        return False
    else:
        l = []
        for c in range(0, 12):
            l.append(codi[c])
        for c in range(0, 12):
            if l[c] not in "0123456789":
                return False
    return True

