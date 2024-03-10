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