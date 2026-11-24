print ("Bienvenido al juego The prisoners dilemma")

print ("modo historia")
print ("modo arcade")
print ("modo multijugador")

def historia():
    print ("eres Leon, tienes 18 años, recien cumplidos, luego de que tu padre desapareciera misterioamente, sin explicar a donde ni por que se iva, te dejo a la deriva, al final lograste encontrar refugio en una habitacion a las afueras de nighy city.")
modo = input("Elige un modo: ")
if modo == "historia":
    historia()
if modo == "arcade":
    print ("modo arcade")
    
if modo == "multijugador":
    print ("modo en proceso; no disponible")
