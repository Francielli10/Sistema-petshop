# Inicio da função cachorro_peso()
def cachorro_peso():
  print(20*'-','| Peso do cachorro |',20*'-')
  while True:
   try:
     cachorropeso= int(input('Digite o peso do cachorro (Kg): '))
     if (cachorropeso <= 3):
      return 40

     elif (cachorropeso >=3) and (cachorropeso < 10): # if (>=3 cachorropeso <10)
      return 50

     elif (cachorropeso >=10) and (cachorropeso < 30): # if (>=10 cachorropeso <30)
      return 60

     elif (cachorropeso >=30) and (cachorropeso < 50): # if (>=30 cachorropeso <50)
      return 70

     else:
      print('Sinto muito não atendemos cachorros maiores que 50 Kg. Digite novamente')
      continue #Irá retronar para o início da pergunta
   except ValueError: # Caso o usuário digite algo incompatível com o que foi pedido, por exemplo letras e números não inteiros.
    print('Digite apenas valores inteiros')
# Fim da função cachorro_peso()

# Inicio da função cachorro_pelo()
def cachorro_pelo():
  print('\n',20*'-', '| Pelo do cachorro |', 20*'-')
  while True:
   cachorropelo=input('Qual o comprimento do pelo do cachorro? \n'+
                      'curto (c)\n'+
                      'médio (m)\n'+
                      'longo (l)\n'+
                      '>> ')
   cachorropelo = cachorropelo.lower()
   cachorropelo = cachorropelo.strip()
   if cachorropelo == 'c':
    return 1.0

   elif cachorropelo == 'm':
    return 1.5

   elif cachorropelo == 'l':
    return 2.0

   else:
    print('Não temos essa opção. Digite novamente')
    continue #Irá voltar para o início do laço (pergunta)
# Fim da função cachorro_pelo()

# Inicio da função cachorro_extra()
def cachorro_extra():
  print('\n',20*'-', '| Serviços Adicionais |', 20*'-')
  acumulador = 0
  while True:
    adicional= input('Deseja algum serviço adicional: \n'+
                     '0 - Não desejo adicional (encerrar pedido) \n'+
                     '1 - Corte de unhas \n'+
                     '2 - Escovar os dentes \n'+
                     '3 - Limpar as orelhas \n'+
                     '>> ')
    if adicional == '0':
      return acumulador

    elif adicional == '1':
      acumulador = acumulador + 10
      continue # Volta para o inicio do laço

    elif adicional == '2':
      acumulador = acumulador + 12
      continue # Volta para o inicio do laço

    elif adicional == '3':
      acumulador = acumulador + 15
      continue # Volta para o inicio do laço
# Fim da função cachorro_extra()

#Inicio do Main
print(15*'-','Bem-vindo ao PetShop da Francielli Fagundes de Souza',15*'-'+'\n')
peso=cachorro_peso()
pelo=cachorro_pelo()
extra=cachorro_extra()
total= peso * pelo + extra
print('\n'+
      43*'-','| TOTAL |',43*'-')
print('\n'+
      'O Valor Total à ser pago é de: R$ {:.2f} (Peso: R$ {:.2f}, Pelo: R$ {:.2f}, Adicional(is): R$ {:.2f})'.format(total, peso, pelo,extra))
