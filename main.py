def pausa():#pausalol
    input("\nPresiona Enter para continuar...")


def elegir(opciones): #funcion para elegir opciones
    for numero, opcion in enumerate(opciones, start=1):
        print(f"{numero}. {opcion}")

    while True:
        respuesta = input("Elige una opción: ")
        if respuesta.isdigit() and 1 <= int(respuesta) <= len(opciones):
            return int(respuesta)
        print(f"Escribe un número del 1 al {len(opciones)}.")


def presentacion_leon(): #presentacion de el prota
    print("\nThe Prisoner's Dilemma — Modo Historia")
    print("Eres Leo. Tienes 18 años.")
    print(
        "Desde que tu padre desapareció, vives en una habitación a las "
        "afueras de Night City. Repartes pedidos y estudias por la noche."
    )
    print(
        "Guardas una libreta de horarios, una llave que ya no abre ninguna "
        "puerta y una fotografía tuya con Nerea."
    )
    print(
        "Nerea es tu mejor amiga. Durante años fue la única persona que sabía "
        "que no tenías adónde volver después de clases."
    )
    pausa()


def acto1(estado): #acto 1 funcion
    print("\nACTO I — LA NOCHE DEL ROBO")
    print(
        "Caminas por un pasillo vacío. En tu mochila llevas la libreta, "
        "una botella de agua y la llave sin llavero."
    )
    print(
        'Nerea te escribió: "Si sigues esperando que alguien decida por ti, '
        'pasarás toda la vida esperando".'
    )
    print('Respondiste: "¿Eso es una invitación o una amenaza?"')
    print('Ella contestó: "Las dos cosas".')
    print(
        "Al final del pasillo, Nerea sostiene una bolsa cerrada. "
        '"Solo será una puerta. Nadie va a salir lastimado", dice.'
    )
    print(
        "Días atrás planearon robar un banco en las afueras de la ciudad. "
        "Ahora, frente a la puerta, el plan parece distinto."
    )
    decision = elegir(
        [
            "Confiar en Nerea y entrar.",
            "Preguntarle qué hay en la bolsa.",
            "Decirle que quieres volver.",
            "Guardar silencio y dejar que ella decida.",
        ]
    )
    match decision: #match case para decisiones acto 1
        case 1:
            estado["rasgos"]["confianza"] += 1
            estado["nerea_confia"] += 1
            print("Nerea te devuelve una sonrisa pequeña. Entran juntos.")
        case 2:
            estado["rasgos"]["control"] += 1
            print("Nerea duda antes de responder. La pregunta queda entre ustedes.")
        case 3:
            estado["rasgos"]["miedo"] += 1
            print("Nerea deja de sonreír, pero no intenta detenerte.")
        case _:
            estado["rasgos"]["miedo"] += 1
            print("Nerea toma tu silencio como una respuesta y abre la puerta.")
    pausa()

    print("\nLas luces rojas parpadean. Se oyen voces al otro lado.")
    decision = elegir(
        [
            "Huir con Nerea.",
            "Intentar cerrar la puerta.",
            "Dejar que Nerea tome la bolsa.",
            "Entregar la bolsa a las autoridades.",
        ]
    )
    match decision: #match case para decisiones acto 1
        case 1:
            estado["rasgos"]["confianza"] += 1
            estado["nerea_confia"] += 1
            print("Corren juntos. Nerea no mira atrás hasta que se quedan sin aire.")
        case 2:
            estado["rasgos"]["control"] += 1
            print("Intentas detener la puerta. Nerea mira la bolsa, no a ti.")
        case 3:
            estado["rasgos"]["sacrificio"] += 1
            estado["nerea_confia"] += 1
            print("Nerea recoge la bolsa. Por un segundo, parece sorprendida de que la dejaras elegir.")
        case _:
            estado["rasgos"]["control"] += 1
            print("Entregas la bolsa. Nerea se queda quieta y dice: \"Eso no era para ti\".")
    pausa()


def acto2(estado): # acto 2 funcion
    print("\nACTO II — LA CÁMARA DE ESPERA")
    print(
        "Despiertas en una habitación blanca. Nerea está al otro lado del "
        "cristal; lleva la misma chaqueta, con una costura rota."
    )
    print(
        "El fiscal Armand deja dos copias del acuerdo sobre la mesa. "
        "\"Si uno confiesa y el otro calla, quien confiesa queda libre. "
        "Si ambos confiesan, reciben dos años. Si ambos callan, uno\"."
    )
    print("En tu celda encuentras una carta sin remitente:")
    print('"Tu silencio puede salvarla. Pero el suyo no es una promesa."')
    decision = elegir(
        [
            "Guardar la carta.",
            "Mostrársela a Nerea.",
            "Entregársela al fiscal.",
            "Romperla.",
        ]
    )
    match decision: #match case para decisiones acto 2
        case 1:
            estado["rasgos"]["miedo"] += 1
            print("La doblas y la escondes. La frase sigue contigo.")
        case 2:
            estado["rasgos"]["confianza"] += 1
            estado["nerea_confia"] += 1
            print("Nerea lee la carta dos veces. No promete nada, pero tampoco se aparta.")
        case 3:
            estado["rasgos"]["control"] += 1
            print("Armand acepta la carta sin sorpresa. Eso te inquieta más que una pregunta.")
        case _:
            estado["rasgos"]["miedo"] += 1
            print("Rasgas la carta. La frase queda en tu memoria.")

    pausa()
    print("\nEn el pasillo, otros presos cuentan lo que eligieron.")
    decision = elegir(
        [
            "Escuchar al que confesó para proteger a su hermano.",
            "Escuchar al que calló y recibió una condena mayor.",
            "Escuchar a la mujer que confesó creyendo a su pareja.",
            "No escuchar a nadie.",
        ]
    )
    match decision: #match case para decisiones acto 2
        case 1:
            estado["rasgos"]["sacrificio"] += 1
            print("\"Lo hice para que mi hermano pudiera volver a casa\", cuenta.")
        case 2:
            estado["rasgos"]["miedo"] += 1
            print("El hombre no se arrepiente de callar. Se arrepiente de confiar.")
        case 3:
            estado["rasgos"]["control"] += 1
            print("La mujer ya no llama traición a lo que hizo. Tampoco lo llama amor.")
        case _:
            estado["rasgos"]["miedo"] += 1
            print("Sigues caminando. Las historias te alcanzan de todos modos.")
    pausa()


def acto3(estado): #acto 3 funcion
    print("\nACTO III — LAS GRIETAS")
    print(
        "Armand coloca una taza vacía sobre la mesa. \"Solo necesito que "
        "recuerdes de quién fue la idea\"."
    )
    decision = elegir(
        [
            "Decir que fue idea tuya.",
            "Decir que fue idea de Nerea.",
            "Decir que no recuerdas.",
            "Decir que ambos lo decidieron.",
        ]
    )
    match decision: #match case para decisiones acto 3
        case 1:
            estado["rasgos"]["sacrificio"] += 1
            print("Armand anota tu respuesta, aunque no parece necesitar escribirla.")
        case 2:
            estado["rasgos"]["control"] += 1
            print("Armand pregunta si estás seguro. No apartas la mirada.")
        case 3:
            estado["rasgos"]["miedo"] += 1
            print("El segundo reloj de la pared marca una hora distinta.")
        case _:
            estado["rasgos"]["confianza"] += 1
            estado["nerea_confia"] += 1
            print("Por primera vez, cuentas la historia como algo que hicieron juntos.")

    print("\nUna pantalla se enciende.")
    print("EL MODELO: \"Tus decisiones no son iguales. Pero sí repetibles\".")
    decision = elegir(
        [
            "Contarle toda la verdad.",
            "Contarle solo algunas partes.",
            "Negarte a hablar.",
            "Intentar engañarlo.",
        ]
    )
    match decision: #match case para decisiones acto 3
        case 1:
            estado["rasgos"]["confianza"] += 1
            estado["nerea_confia"] += 1
            print("EL ARTEFACTO: \"Todavía hay información que no te han dicho.\"")
        case 2:
            estado["rasgos"]["control"] += 1
            print("EL ARTEFACTO: Cada verdad puede convertirse en una mentira si se usa tarde.")
        case 3:
            estado["rasgos"]["miedo"] += 1
            print("EL ARTEFACTO: Puedo esperarte. No significa que Armand vaya a hacerlo.")
        case _:
            estado["rasgos"]["control"] += 1
            print("EL ARTEFACTO repite tu respuesta con tu propia voz.")
    pausa()


def acto4(estado): #acto 4 funcion
    print("\nACTO IV — EL PRECIO DE LA CONFIANZA")
    print(
        "Nerea está sentada frente a la puerta de su celda. No está "
        "bromeando. \"Si confieso, tú puedes irte. Si confiesas, yo puedo irme\"."
    )
    decision = elegir(
        [
            "Proponer que ambos guarden silencio.",
            "Proponer que ambos confiesen.",
            "Pedirle a Nerea que confiese.",
            "Decir que tú asumirás la culpa.",
            "Romper el trato y enfrentarse al fiscal.",
        ]
    )
    match decision: #match case decisiones acto 4
        case 1:
            estado["rasgos"]["confianza"] += 1
            estado["nerea_confia"] += 1
            print("Nerea asiente, pero no promete que mantendrá el silencio.")
        case 2:
            estado["rasgos"]["confianza"] += 1
            estado["nerea_confia"] += 1
            print("\"Al menos sería una decisión de los dos\", dice Nerea.")
        case 3:
            estado["rasgos"]["control"] += 1
            print("Nerea aparta la mirada. \"No me pidas que haga eso por ti\".")
        case 4:
            estado["rasgos"]["sacrificio"] += 1
            estado["nerea_confia"] += 1
            print("\"No necesito que me salves\", dice. Esta vez no suena enfadada.")
        case _:
            estado["rasgos"]["confrontacion"] += 1
            print("\"Las dos decisiones son parte de una prueba\", dices. Nerea mira la cámara.")
    pausa()


def elegir_modelo(rasgos): #funcion para elegir modelo en arcade
    docil = rasgos["confianza"] + rasgos["sacrificio"]
    agresivo = rasgos["control"] + rasgos["confrontacion"]
    indeciso = rasgos["miedo"]

    if docil > agresivo and docil > indeciso:
        return "dócil"
    if agresivo > docil and agresivo > indeciso:
        return "agresivo"
    return "neutral"


def jugar_dilema(modelo, primera_eleccion=None, permitir_salir=False):#bucle jugable
    print(f"\nEL ARTEFACTO se presenta como {modelo}.")
    match modelo:
        case "dócil":
            print("Busca evitar el daño y guarda silencio en cada ronda.")
        case "agresivo":
            print("Usa lo que aprendió de ti y confiesa en cada ronda.")
        case _:
            print("No se define: empieza en silencio y repite tu decisión anterior.")

    print("\nEl primero en conseguir cinco victorias gana.")
    print("Si ambos eligen lo mismo, nadie suma un punto.")
    leo = 0
    rival = 0
    eleccion_anterior = "guardar silencio"
    ronda = 0
    opciones = ["Confesar el delito.", "Guardar silencio."]
    if permitir_salir:
        opciones.append("Dejar de jugar y volver al menú.")

    while leo < 5 and rival < 5: #bucle jugable
        ronda += 1
        if ronda == 1 and primera_eleccion is not None:
            eleccion_leo = primera_eleccion
        else:
            decision = elegir(opciones)
            if permitir_salir and decision == 3:
                print("\nSales del modo arcade.")
                return None
            eleccion_leo = "confesar" if decision == 1 else "guardar silencio"

        match modelo:#match case para el modelo (artefacto)
            case "dócil":
                eleccion_modelo = "guardar silencio"
            case "agresivo":
                eleccion_modelo = "confesar"
            case _:
                eleccion_modelo = eleccion_anterior

        print(f"\nRonda {ronda}: tú eliges {eleccion_leo}.")
        print(f"EL ARTEFACTO elige {eleccion_modelo}.") #artefacto==modelo, cambio solicitado por dilan, gracias cpsito
        match eleccion_leo, eleccion_modelo:
            case "confesar", "guardar silencio":#match case para elecciones
                leo += 1
                print("Tú quedas libre y EL ARTEFACTO recibe tres años. Punto para ti.")
            case "guardar silencio", "confesar":
                rival += 1
                print("EL ARTEFACTO queda libre y tú recibes tres años. Punto para EL ARTEFACTO.")
            case "confesar", "confesar":
                print("Ambos confiesan: reciben dos años. Nadie suma un punto.")
            case _:
                print("Ambos guardan silencio: reciben un año. Nadie suma un punto.")

        eleccion_anterior = eleccion_leo
        print(f"Marcador — Leo: {leo} | EL ARTEFACTO: {rival}")

    return leo > rival


def acto5(estado): #acto 5 funcion FINAL
    print("\nACTO V — LA ELECCIÓN FINAL")
    print("Armand deja un documento frente a ti. \"Puedes confesar o negar "
        "todo. Si la otra parte habla, recibirás tres años. Si ambos "
        "confiesan, dos. Si ambos callan, uno\"."
    )
    print("EL ARTEFACTO: \"Así funciona su justicia\".")
    primera_eleccion = elegir(["Confesar el delito.", "Guardar silencio."])
    primera_eleccion = "confesar" if primera_eleccion == 1 else "guardar silencio"

    modelo = elegir_modelo(estado["rasgos"])
    gano_leo = jugar_dilema(modelo, primera_eleccion)

    print("\nEPÍLOGO")
    if gano_leo: # en caso de que prota gane
        print("Leo llega primero a cinco victorias. EL ARTEFACTO deja de hablar.")
        if estado["nerea_confia"] >= 3:
            print("Nerea espera al otro lado de la puerta. Esta vez, eliges abrirla.")
        else:
            print("Sales libre. La cámara no te sigue, pero tampoco olvidas que estaba allí.")
        print("Armand no destruye el acuerdo. Por primera vez, deja que decidas qué hacer con él.")
    else: #en caso de que prota pierda
        print("EL ARTEFACTO llega primero a cinco victorias.")
        match modelo: #matchcase para el modelo
            case "agresivo":
                print("\"Aprendí de tus acusaciones\", dice. La voz suena demasiado parecida a la tuya.")
            case "dócil":
                print("\"Podías haber confiado\", dice. No sabes si habla por ti o por Nerea.")
            case _:
                print("EL ARTEFACTO guarda silencio. Armand firma los documentos por los dos.")
        print("Nerea no está en la sala. El acuerdo no dice qué decidió ella.")


def historia():# modo historia funcion
    estado = {
        "rasgos": {
            "confianza": 0,
            "control": 0,
            "miedo": 0,
            "sacrificio": 0,
            "confrontacion": 0,
        },
        "nerea_confia": 0,
    }
    presentacion_leon()
    acto1(estado)
    acto2(estado)
    acto3(estado)
    acto4(estado)
    acto5(estado)


def modo_arcade(): #inicio de modo arcade
    print("\nMODO ARCADE")
    decision = elegir(
        [
            "Jugar contra el modelo dócil.",
            "Jugar contra el modelo neutral.",
            "Jugar contra el modelo agresivo.",
            "Volver al menú.",
        ]
    )
    if decision == 4:
        return

    modelos = {1: "dócil", 2: "neutral", 3: "agresivo"}
    modelo = modelos[decision]
    print(f"\nHas elegido el modelo {modelo}.")
    print("Cada partida termina cuando alguien consigue cinco victorias.")
    print("Puedes salir en cualquier ronda; al terminar una partida, empieza otra.")

    while True:
        gano_el_jugador = jugar_dilema(modelo, permitir_salir=True)
        if gano_el_jugador is None:
            return
        if gano_el_jugador:
            print("\n¡Ganaste la partida!")
        else:
            print("\nEL MODELO ganó la partida.")
        print("Marcador reiniciado para la siguiente partida.")


def modo_de_juego():#inicio de juego elegir
    while True:
        print("\nBienvenido a The Prisoner's Dilemma")
        print("Modos disponibles: historia, arcade, multijugador, salir")
        modo = input("Elige un modo: ").strip().lower()

        match modo:#match case modo historia, arcade, multijugador, salir
            case "historia":
                historia()
                return
            case "arcade":
                modo_arcade()
            case "multijugador":
                print("El modo multijugador todavía no está disponible.")
            case "salir":
                print("Gracias por jugar.")
                return
            case _:
                print("Opción no reconocida. Elige historia, arcade, multijugador o salir.")


if __name__ == "__main__": #para main
    modo_de_juego()
