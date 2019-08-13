#CÓDIGO EM MICROPYTHON TOMANDO COMO BASE PROJETO MOVIMENTOCIRCULAR DO PROGRAMA URA

from machine import Pin #utilização de pinos numerados da placa
import pyb #class de auxiliar de Servomotor da porta X1-X4
import time

"""#import umqtt "biblioteca de utilização mqtt"
qos(1) --> quality of service ao menos uma vez
"""

#substituivel pelo umqtt
xsinal=machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP) #numero do pino por onde vem a comunicação wifi
#ou um de um import da json ou network_modules
#available Pins = 0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16"""

#========= DEFNIÇÃO DE GLOBALS =========# 

sensor = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
estado_sensor=False

roda_esquerda = pyb.Servo(0,machine.Pin.OUT)
roda_direita = pyb.Servo(2,machine.Pin.OUT)

n_experimento = 0
volta = 0
tempo_volta

raio = []
angulo = []
vel_angular = []
vel_linear = []

#========= UMQTT SINAL =========# 


#========= COMANDOS DOS SERVO MOTORES =========# 

#??pyb.Servo.speed(valor) ==>valor de -100 até 100

def re():
	roda_direita.Servo.speed(100)
	roda_esquerda.Servo.speed(-100)
	pass
def frente():
	roda_direita.Servo.speed(-100)
	roda_esquerda.Servo.speed(100)
	pass
def parado():
	#detach pin...?
	#roda_direita.Servo.speed(-100)
	#roda_esquerda.Servo.speed(100)
	pass
def esquerda():
	roda_direita.Servo.speed(0)
	roda_esquerda.Servo.speed(100)
	pass
def direita():
	roda_direita.Servo.speed(-100)
	roda_esquerda.Servo.speed()
	pass

#========= COMANDOS =========#
def comando_read_alpha():
		xsinal()
		#testa se sinal recebido é caracter (wsad)
		if xsinal.isalpha():
			return xsinal

def comando_read_num():
		xsinal()
		
		if isinstance(xsinal,int):
			return xsinal

def comando_list(comando):
	if comando is 'a':
		esquerda()
		pass
	elif comando is 's':
		re()
		pass
	elif comando is 'w':
		frente()
		pass
	elif comando is 'd':
		direita()
		pass
	elif comando is 'p':
		imprimir_experimento()
		pass
	elif comando is 'r':
		()###############
		pass		
	elif comando is 'q':
		()###############
		pass
	else :
		parado()
		pass

#========= CONTADOR DE VOLTAS POR SENSOR =========#	

def mudanca_sensor():
	if sensor.value() is True and estado_sensor is False :
		return True
	if sensor.value() is False and estado_sensor is True:
		return True
	return False
	pass

def conta_volta():
	if volta is 0:
		tempo = time.ticks_ms() 
	volta+1
	if volta is 3:
		tempo_volta = time.ticks_diff(time.ticks_ms(), tempo) /1000.0
		parado()
		console_dados()
		volta = 0
		n_experimento+1
	pass

#========= CONSOLE =========#	

def console_dados():
	print(n_experimento,':',tempo_volta,'segundos')
	#if n_experimento >= 1000:  #calular limite de memória
		#print("Memoria de dados cheia")
	#else:
		print("Insira a medida de Raio em centimetros")
		raio.append(comando_read_num()/100)
		print("Insira a medida entre ({0 e 360}) em graus")
		angulo.append(comando_read_num()%361) #limitação em 360 graus
		vel_angular.append( ( (angulo(n_experimento)/180) * PI) / tempo_volta )
		vel_linear.append( vel_angular(n_experimento) * raio(n_experimento) )
		pass
	pass

def imprimir_experimento():
	for i in xrange(0,n_experimento):
		pass
	 
    if ((raio(i) == 0.00 || angulo(i) == 0.00 || vAngular(i) == 0.00 || vLinear(i) == 0.00))
      break
    print(i + 1,':: Raio = ',raio(i),'m ; Angulo = ',angulo(i),'º ; Velocidade Angular = ',vAngular(i),'rad/s ; Velocidade Linear = ',vLinear(i),' m/s ')
	pass

#========= MAIN =========#	

while 1:

	comando_list(comando_read_alpha())
	if mudanca_sensor() is True:
		conta_volta()	

	pass

#========= PROBLEMAS =========#	
#IMPLEMENTAR FUNÇÃO DE RECOMEÇO DE EXPERIMENTO -->COMANDO_LIST
#IMPLEMENTAR FUNÇÃO DE APAGAR N_EXPERIMENTO ESPECIFICO -->COMANDO_LIST
#DESCOBRIR ONDE SE ENCAIXA CONSOLE_DADOS()
#LIMITAR VALOR DA LEITURA DE DADOS #CALCULAR O LIMITE DE LISTAS NA MEMORIA ESPECIFICA PARA CADA ESP8266 -->GET.EXPERIMENTO
#DESCOBRIR METODO DE LEITURA DE MQTT PARA TERMINAL DE COMANDO
#TROCAR TODOS OS PRINTS POR COMUNICAÇÃO UMQTT

#TESTAR CÓDIGO EM MICROPYTHON PARA ESP8266
