#Actividad 2 - Primeros auxilios
#   En cualquier momento puede haber una emergencia y hay que estar preparados ¿sabrías cómo reaccionar en caso
#   de que alguien necesite de primeros auxilios?
#   Es muy probable que mucha gente no conozca cuáles son los pasos a seguir en caso de emergencia. 
#   Es por eso que se le solicita construir una aplicación que permita indicar los pasos a seguir ante una emergencia.
#   Debido a que no se espera que usted sea un experto en el tema se le provee de un diagrama que explica las 
#   distintas instancias a la que se está sometido durante una emergencia.

#  Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que entregue los distintos 
#  pasos a seguir dependiendo de las respuestas que el usuario entrega en tiempo real.

estado = input("¿Responde a Estímulos? ")
if estado.lower() == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
else:
    print("Abrir la vía Aérea") 

respira = input("¿Respira? ")
if respira.lower() == "si":  
    print("Permitirle posición de suficiente ventilación")
else:
    print("Administrar 5 ventilaciones y llamar a la ambulancia")

signos_vitales = input("¿Tiene signos vitales? ")
if signos_vitales.lower() == "si": 
   print("Reevaluar a la espera de la ambulancia")
else:
   print("Administrar compresiones torácicas hasta que llegue la ambulancia")
 
ambulancia = input("¿Llegó la ambulancia? ") 
while ambulancia.lower() == "no":
    signos_vitales = input("¿Tiene signos vitales? ")
    if signos_vitales.lower() == "no":
        print("Administrar compresiones torácicas hasta que llegue la ambulancia") 
    else:
        print("Reevaluar a la espera de la ambulancia")
    ambulancia = input("¿Llegó la ambulancia? ")

if ambulancia.lower() == "si":
    print("Pronta recuperación")
