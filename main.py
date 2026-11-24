print ("Bienvenido al juego The prisoners dilemma")

print ("modo historia")
print ("modo arcade")
print ("modo multijugador")

def historia():
    print("=====================================")
    print("eres Leon, tienes 18 años, recien cumplidos, luego de que tu padre desapareciera misterioamente, sin explicar a donde ni por que se iva, te dejo a la deriva, al final lograste encontrar refugio en una habitacion a las afueras de nighy city.")
    print("=====================================")
    input(" ")
    print("=====================================")
    print("trabajas repartiendo pedidos, estudiando de noche y conservando un cuan de cosas importantes; una libreta de horarios, una llave que ya no abre a ningun ldo, y una fotografia entrecortada, de ti con narea")
    print("=====================================")
    
modo = input("Elige un modo: ")
if modo == "historia":
    historia()
if modo == "arcade":
    print ("modo arcade")
    
if modo == "multijugador":
    print ("modo en proceso; no disponible")
