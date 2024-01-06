from random import randint

def alistar(condicion,pasador,diccionario): #Función para anidar las columnas en un solo grupo
    if condicion == "1":
        for k in range (7):
            pasador.append(diccionario["2"][k])
        for k in range(7):
            pasador.append(diccionario["1"][k])
        for k in range(7):
            pasador.append(diccionario["3"][k])
    elif condicion == "2":
        for k in range (7):
            pasador.append(diccionario["1"][k])
        for k in range(7):
            pasador.append(diccionario["2"][k])
        for k in range(7):
            pasador.append(diccionario["3"][k])
    elif condicion == "3":
        for k in range (7):
            pasador.append(diccionario["2"][k])
        for k in range(7):
            pasador.append(diccionario["3"][k])
        for k in range(7):
            pasador.append(diccionario["1"][k])
    
    diccionario["1"].clear(),diccionario["2"].clear(),diccionario["3"].clear()

def ordenar(diccionario,pasador): #Función para desagrupar el conjunto de cartas a las distintas columnas
    for m in range(21):
        if m in [0,3,6,9,12,15,18]:
            diccionario["1"].append(pasador[0])
            pasador.pop(0)
        elif m in[1,4,7,10,13,16,19]:
            diccionario["2"].append(pasador[0])
            pasador.pop(0)
        else:
            diccionario["3"].append(pasador[0])
            pasador.pop(0)

cartas = ["A◊","2◊","3◊","4◊","5◊","6◊","7◊","8◊","9◊","10◊","J◊","Q◊","K◊",
         "A♤","2♤","3♤","4♤","5♤","6♤","7♤","8♤","9♤","10♤","J♤","Q♤","K♤",
         "A♧","2♧","3♧","4♧","5♧","6♧","7♧","8♧","9♧","10♧","J♧","Q♧","K♧",
         "A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥"] #Las 52 cartas para randomizar

fila_1 = []
fila_2 = []
fila_3 = []
descartador = [] #Sirve para poder mover los datos más fácil


#Esto es para que las cartas siempre sean random
for i in range (7): 
    descartador.append(cartas[randint(0,51)])
    while descartador[0] in fila_1:
        descartador.pop()
        descartador.append(cartas[randint(0,51)])
    fila_1.append(descartador[0])
    descartador.pop()

    descartador.append(cartas[randint(0,51)])
    while descartador[0] in fila_1 or descartador[0] in fila_2:
        descartador.pop()
        descartador.append(cartas[randint(0,51)])
    fila_2.append(descartador[0])
    descartador.pop()

    descartador.append(cartas[randint(0,51)])
    while descartador[0] in fila_1 or descartador[0] in fila_2 or descartador[0] in fila_3:
        descartador.pop()
        descartador.append(cartas[randint(0,51)])
    fila_3.append(descartador[0])
    descartador.pop()



orden = {"1":fila_1,"2":fila_2,"3":fila_3}
movedor = [] #Para mover datos sin perder otros


print("\nEscoge una carta, trataré de adivnarlo\n-----------------------")
for j in range(7):
    print(f"{orden['1'][j]}\t{orden['2'][j]}\t{orden['3'][j]}") #Inicio
print("-----------------------")

while True:
    att_1 = input("\n¿En que columna está tu carta? --> ")

    if att_1 in ["1","2","3"]:
        alistar(att_1,movedor,orden)
        ordenar(orden,movedor)
        break
    
    else: print("--Elija una columna correcta--")


print("\n-----------------------")
for j in range(7):
    print(f"""{orden['1'][j]}\t{orden['2'][j]}\t{orden['3'][j]}""") # Mezclado ya una vez
print("-----------------------")

while True:
    att_2 = input("¿En qué columna se encuentra ahora tu carta?")

    if att_2 in ["1","2","3"]:
        alistar(att_2,movedor,orden)
        ordenar(orden,movedor)
        break
    else: print("--Elija una columna correcta--")


print("\n-----------------------")
for j in range(7):
    print(f"""{orden['1'][j]}\t{orden['2'][j]}\t{orden['3'][j]}""") #Mezclado ya 2 veces
print("-----------------------")

while True: 
    att_3 = input("¿En qué columna se encuentra tu carta ahora?")

    if att_3 in ["1","2","3"]: #Procesando última mezcla y ya no se mostrará el menú sino la carta en la que pensó
        alistar(att_3,movedor,orden)
        break
    else: print("--Elija una columna correcta--")


print(f"\n TU CARTA ES --> {movedor[10]}\n")
