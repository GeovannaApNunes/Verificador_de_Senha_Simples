senha = '0000'
tentativas = 3
while tentativas !=0:
  tentativa = input("Digite uma senha numerica de quatro digitos: ")

  if tentativa == senha:
    print("Senha correta. Acesso concedido")
    break

  else:
    print("Senha incorreta. Tente")
    tentativas -= 1