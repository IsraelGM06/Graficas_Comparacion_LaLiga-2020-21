


def llenarData(data,id,jugadores):
# Esta función pide como parámetros "data" que serían los "DataFrame" que vamos a rellenar, el "id" que es el código de cada equipo
# y el  diccionario de jugadores de el equipo
    jugadorLoc=1
    # Esta variable "jugadorLoc" va a ser el índice con el que estaremos rellenando las filas de el "DataFrame"
    for jugador in range(len(jugadores)):
        numJugador=str(jugador+1)
        # Esta variable "numJugador" se juntara con "id" para acceder a la información de cada jugador
        if(jugadores[id+numJugador]["posicion"]=="POR"):
        # La forma en la que se rellenaran son diferentes, si es portero o no
        # Cambia en la forma de rellenar la columna de goles, asistencias y paradas, 
            data.loc[jugadorLoc]=[id+numJugador,jugadores[id+numJugador]["nombre"],jugadores[id+numJugador]["edad"],jugadores[id+numJugador]["numero"],
            jugadores[id+numJugador]["partidos"],0,0,jugadores[id+numJugador]["paradas"],
            jugadores[id+numJugador]["nacionalidad"],jugadores[id+numJugador]["posicion"]]
        else:
            data.loc[jugadorLoc]=[id+numJugador,jugadores[id+numJugador]["nombre"],jugadores[id+numJugador]["edad"],jugadores[id+numJugador]["numero"],
            jugadores[id+numJugador]["partidos"],jugadores[id+numJugador]["goles"],jugadores[id+numJugador]["asistencias"],0,
            jugadores[id+numJugador]["nacionalidad"],jugadores[id+numJugador]["posicion"]]
        jugadorLoc+=1
        

