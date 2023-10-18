usario = input("Nome de Usuário: ")
senha = input("Digite a senha: ")
while usario == senha:
    print("A senha e usuário não podem ser os mesmos, bobão!")
    usario = input("Digite o user novamente: ")
    senha = input("Digite a senha novamente: ")