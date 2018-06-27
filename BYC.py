# Juego Bulls&Cows/ Toros y Vacas
# Roberto Chen Zheng

from random import randint

def Reglas():
    print("\nEl objetivo:\nAdivinar el número al azar de n dígitos")
    print("Las cifras son todas diferentes")
    print("Toro: Si una cifra está presente y se encuentra en el lugar correcto")
    print("Vaca: Si una cifra está presente pero se encuentra en un lugar equivocado")
    print("Al adivinarse el número se termina la partida")
    print("Los números a utilizar son del 0-9\n")
    print("El número a adivinar no puede empezar con el número 0")
    return

#Verifica que los numeros generados no estén repetidos
#Recibe una lista
#Devuelve un True si hay repetidos, y False si no hay repetidos
def Repetidos(lista):
    #Se verifica con el largo de la lista
    return(len(lista) != len(set(lista))) 

    
# Generador de numeros aleatorios para cierta dificultad
    # Falta verificar que no se repitan numeros
    # Son retornados como una lista de numeros separados ejm: [3,2,4,1]
def Generador(num):
    repetido= True
    if (num==1):
        while(repetido == True):
            rando= randint(100,999)
            lista= [int(i) for i in str(rando)]
            repetido= Repetidos(lista)
        return (lista)
    elif (num==2):
        while(repetido == True):
            rando= randint(1000,9999)
            lista= [int(i) for i in str(rando)]
            repetido= Repetidos(lista)
        return (lista)
    elif (num==3):
        while(repetido == True):
            rando= randint(10000,99999)
            lista= [int(i) for i in str(rando)]
            repetido= Repetidos(lista)
        return (lista)
    else:
        return ([])


def Evaluacion(numero,var,respuesta):
    toros=0
    vacas=0
    index=0
    if (len(numero) == len(respuesta)):
        for i in range(0,len(respuesta)):
            if (respuesta[i] == numero[i]):
                toros+= 1
            elif (numero[i] in respuesta):
                vacas+= 1
        return(toros, vacas)
    else:
        print("Mensaje de Error en funcion Evaluacion: Listas diferente tamaño")

def Nivel_1():
    print("Juego Fácil 3 dígitos")
    contador=0
    var= False
    respuesta= Generador(1)
    print(respuesta)
    while (var==False):
        numero= IngresarDatos()
        resultado= Evaluacion(numero,var,respuesta)
        DeployMessage(resultado)
        if(resultado[0]==3):
            var= True
    else:
        DeployWinnerMessage(respuesta)



def IngresarDatos():
    numero= input("Ingrese el numero: ")
    lista= [int(i) for i in str(numero)]
    return (lista)
    
    
def DeployMessage(resultado):
    print("Usted tiene "+ str(resultado[0])+ " toros y " + str(resultado[1]) +" vacas")

def DeployWinnerMessage(respuesta):
    print("Usted ha ganado la respuesta es: " + str(respuesta))
    

def BYC():
    print("*** Bulls & Cows ***")
    print("1. Jugar \n2. Reglas \n3. Salir")
    opcion= int(input("Seleccione una opción: "))
    if (opcion == 1):
        nivel= input("Ingrese la dificultad: ")
        if (nivel == 1):
            Nivel_1()
        elif (nivel == 2):
            Nivel_2()
        elif (nivel ==3):
            Nivel_3()
        else:
            print ("Elija de nuevo la dificultad: ")
    elif (opcion == 2):
        Reglas()
        BYC()
    elif (opcion == 3):
        print("Bye Bye")
