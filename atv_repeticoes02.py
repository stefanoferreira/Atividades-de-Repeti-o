#Faça um programa que leia um nome de usuário e a sua senha e não aceite
#a senha igual ao nome do usuário, mostrando uma mensagem de erro e 
#voltando a pedir as informações.


while True:
    
    nome_usuario = input("Digite um nome de usuário:")
    
    senha = input("Digite sua senha:")
    
    if nome_usuario == senha:
        print(f"Senha ou Usuário incorretos, por favor repita a operação!")
        
    else:
        break
    
    
    
    