#1-Verificação de números diferentes
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))

if n1 != n2:
  print('Os números são diferentes')
else:
  print('Os números são iguais')

#2-Verificação de maioridade
idade = int(input('Insira a idade: '))

if idade >= 18:
  print('Maior de idade')
else:
  print('Menor de idade')

#3-Autorização de entrada em um evento
convite = input('Apresente o convite: ').upper().strip()

if convite == '2025':
  print('Entrada permitida')
else:
  print('Entrada Negada')

#4-Verificação de nome em lista
nome = input('Insira o nome: ').upper().strip()

if nome == 'CARLOS':
  print('Você está na lista')
else:
  print('Nome não encontrado')

#5-Cálculo de gorjeta
conta = float(input('Insira o Valor: '))
if conta > 100.00:
  gorjeta = conta * 0.1
  print(f'O Valor a pagar e de: {conta:.2f}', f'E a gorjeta e de: {gorjeta:.2f}')
else:
  gorjeta = conta * 0.05
  print(f'O Valor a pagar e de: {conta:.2f}', f'E a gorjeta e de: {gorjeta:.2f}')

#6-Acesso ao Wi-Fi
senha = input('Senha do Wi-fi: ')
if senha == 'SENHA123':
  print('Conectado')
else:
  print('Senha incorreta')

#7-Verificação de turno
turno = input('digitar M para manhã ou qualquer outra tecla para tarde: ').upper().strip()
if turno == 'M':
  print('Bom dia')
else:
  print('Boa tarde')

#8-Verificação de múltiplo de 5
multiplo = int(input('Insira um numero: '))
if multiplo % 5 == 0:
  print('Numero Multiplo de 5')
else:
  print('Não é Multiplo de 5')

#9-Desconto em compras por valor mínimo
compra = float(input('Insira o valor: '))
if compra > 150.00:
    print('O valor é: ', compra - 20.00)
else:
    print('O valor é: ', compra)
