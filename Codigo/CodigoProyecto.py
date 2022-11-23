
from codigoBloquesProyecto import *
i=0
nbRun=1 #numero de veces que quieres que se repita el ciclo
tiempoEspera=1 #aqui puedes editar esta variable de tiempo de espera
while i<nbRun:
    
    #poner codigo aqui
    #    abrirPuerta#()
    #    cerrarPuerta#()
    #    esperar(TIEMPO EN SEGUNDOS)
    if(leerSensores() == 5):
        abrirPuerta(5)
        esperar(1)
        cerrarPuerta(5)
    if(leerSensores() == 8):
        abrirPuerta(8)
        esperar(1)
        cerrarPuerta(8)
    if(leerSensores() == 4):
        abrirPuerta(4)
        esperar(1)
        cerrarPuerta(4)
    
    

 


    

  
