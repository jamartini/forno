umidade = float(input('LEITURASENSOR(UMIDADE)'))
temp_atual = float(input('LEITURASENSOR(TEMPERATURA)'))
tempo_decorrido = 0
tempo_coccao = 0

def exaustor(modo) :
 if modo == 'on' :
   return 'exaustor ativado'
 elif modo == 'off' :
    return 'exaustor desativado'

def aquecimento(modo) :
  if modo == 'on' :
    return 'aquecimento ativado'
  elif modo == 'off' :
    return 'aquecimento desativado'

def timer(modo) :
  if modo == 'set' :
    return 'temporizador ativado'
  elif modo == 'reset' :
    return 'temporizador zerado'
  elif modo == tempo_coccao :
    while tempo_decorrido < tempo_coccao :
      return 'temporizador ativado'

def botao(modo) :
  if modo == 'on' :
    return 'botão ativado'
  elif modo == 'off' :
    return 'botão desativado'  

if umidade >= 40 and temp_atual <= 20 :
  inverno = True
else :
  inverno = False

if inverno == True :
  print('Início desumidificação')
  if temp_atual >= 15 :
    exaustor('on')
  else :
    exaustor('on')
    aquecimento('on')
  if temp_atual >= 100 :
    aquecimento('off')
  if umidade <= 5 :
    exaustor('off')
    aquecimento('off')

print('Início cocção')
if umidade > 15 :
  exaustor('on')
if temp_atual < 200 :
  aquecimento(380)
if umidade <= 5 :
  exaustor('off')
if umidade <= 5 and temp_atual == 380 :
  print('Inserir conteúdo para cocção. Após, pressionar o botão PRONTO')

if botao('on'):
  #Aqui o 1/6 representa os 10s (1/6 de minuto) em que o forno faz a leitura do programa, ou seja, a cada vez que o forno lê o programa são adicionados os 10 segundos passados à variável tempo_decorrido
  tempo_decorrido += 1/6
  tempo_coccao = 180
  timer(tempo_coccao)
  if tempo_decorrido == tempo_coccao :
    aquecimento('off')
    print('Cocção concluída')