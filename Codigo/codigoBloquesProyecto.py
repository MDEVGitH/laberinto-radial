import RPi.GPIO as GPIO
import time
  
#Setup servoPin as PWM output of frequancy 100Hz
servoPin1=12
servoPin2=8
servoPin3=10
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

#setup sweep parameters
depart =0
arrivee=45
DELAY=0.1
incStep=5
pos=depart


def abrirPuerta(pinIn):
    
    if(pinIn==1):
        var = 8
    elif(pinIn==2):
        var=10
    elif(pinIn==3):
        var=12
    elif(pinIn==4):
        var=16
    elif(pinIn==5):
        var=18
    elif(pinIn==6):
        var=22
    elif(pinIn==7):
        var=24
    elif(pinIn==8):
        var=26
    else:
        print("Motor seleccionado no existe")
        
    servoPin1=var
    print("Abriendo puerta: " + str(pinIn))
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin1,GPIO.OUT)
    
    pwm1=GPIO.PWM(servoPin1,100)
    pwm1.start(0) #star pwm
    for pos in range(depart,arrivee,incStep*2):
        
        duty=float(pos)/10.+5.
        pwm1.ChangeDutyCycle(duty)
        time.sleep(DELAY)
    pwm1.stop()
    time.sleep(0.5)
    GPIO.cleanup()
    
     
    
def cerrarPuerta(pinIn):
    if(pinIn==1):
        var = 8
    elif(pinIn==2):
        var=10
    elif(pinIn==3):
        var=12
    elif(pinIn==4):
        var=16
    elif(pinIn==5):
        var=18
    elif(pinIn==6):
        var=22
    elif(pinIn==7):
        var=24
    elif(pinIn==8):
        var=26
    else:
        print("Motor seleccionado no existe")
    servoPin1=var
    print("Cerrando puerta: " + str(pinIn))
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin1,GPIO.OUT)
    pwm1=GPIO.PWM(servoPin1,100)
    pwm1.start(float(90)/10.+5.) #star pwm
    for pos in range(arrivee,depart,-incStep):
        duty=float(pos)/10.+5.
        pwm1.ChangeDutyCycle(duty)
        time.sleep(DELAY)
     #stop sending value to output
    
    pwm1.stop()
    time.sleep(0.5)
    GPIO.cleanup()

def leerSensores():
    sensor = False
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3,GPIO.IN)
    GPIO.setup(5,GPIO.IN)
    GPIO.setup(7,GPIO.IN)
    GPIO.setup(11,GPIO.IN)
    GPIO.setup(13,GPIO.IN)
    GPIO.setup(15,GPIO.IN)
    GPIO.setup(19,GPIO.IN)
    GPIO.setup(21,GPIO.IN)    
    
    while (sensor == False):
        print("Leyendo...")
        if(not GPIO.input(3)):
            sensor=True
            print("sensor 1 detectado...")
            return 1
        elif(not GPIO.input(5)):
            sensor=True
            print("sensor 2 detectado...")
            return 2
        elif(not GPIO.input(7)):
            print("sensor 3 detectado...")
            sensor=True
            return 3
        elif(not GPIO.input(11)):
            print("sensor 4 detectado...")
            sensor=True
            return 4
        elif(not GPIO.input(13)):
            print("sensor 5 detectado...")
            sensor=True
            return 5
        elif(not GPIO.input(15)):
            print("sensor 6 detectado...")
            sensor=True
            return 6
        elif(not GPIO.input(19)):
            print("sensor 7 detectado...")
            sensor=True
            return 7
        elif(not GPIO.input(21)):
            print("sensor 8 detectado...")
            sensor=True
            return 8
        else:
            sensor = True
            return 0
        
            
        
    
def esperar(tiempo):
    time.sleep(tiempo)
    