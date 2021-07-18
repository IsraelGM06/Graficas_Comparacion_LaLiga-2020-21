import pandas as pd
import jugadores
import funciones
from bokeh.models import  ColumnDataSource


dataBarca= pd.DataFrame(columns=("ID","nombre" ,"edad","numero","partidos","goles","asistencias","paradas","nacionalidad","posicion"))
# Creamos "DataFrame" con las columnas de los datos de los jugadores
dataRealMadrid= pd.DataFrame(columns=("ID","nombre" ,"edad","numero","partidos","goles","asistencias","paradas","nacionalidad","posicion"))
dataAtleticoMadrid= pd.DataFrame(columns=("ID","nombre" ,"edad","numero","partidos","goles","asistencias","paradas","nacionalidad","posicion"))
dataAthleticClub= pd.DataFrame(columns=("ID","nombre" ,"edad","numero","partidos","goles","asistencias","paradas","nacionalidad","posicion"))


funciones.llenarData(dataBarca,"JB",jugadores.jugadoresBarca)
# Con esta función que se encuentra en el archivo "funciones.py", llenamos los "DataFrame" de cada equipo con los datos que
# se encuentran en el archivo "jugadores.py"
funciones.llenarData(dataRealMadrid,"JRM",jugadores.jugadoresRealMadrid)
funciones.llenarData(dataAtleticoMadrid,"JAM",jugadores.jugadoresAtleticoMadrid)
funciones.llenarData(dataAthleticClub,"JAC",jugadores.jugadoresAthleticClub)

xp="partidos"
yp="goles"
# Estas variables son los valores de x / y que se evalúan al iniciar

############## Atletico Madrid ################################
sourceAtleticoMadrid = ColumnDataSource(data=dict(
        # Creamos un "ColumnDataSource" con la información de cada equipo
        partidos = dataAtleticoMadrid["partidos"],
        goles = dataAtleticoMadrid["goles"],
        paradas = dataAtleticoMadrid["paradas"],
        asistencias = dataAtleticoMadrid["asistencias"],
        edad = dataAtleticoMadrid["edad"],
        numero = dataAtleticoMadrid["numero"],
        # Primero están los datos de todas las opciones de comparación para que se pueda acceder a estos datos al cambiar
        # la opción en el selector
        x=dataAtleticoMadrid[xp],
        y=dataAtleticoMadrid[yp],
        # x / y son los datos de los valores iniciales
        nombre=dataAtleticoMadrid.nombre,
        posicion = dataAtleticoMadrid.posicion,
        nacionalidad = dataAtleticoMadrid.nacionalidad
        # Estos últimos 3 datos sirven para mostrarlos cuando el cursor este encima de un circulo junto con X/Y
    ))

    ############## Barca ################################
sourceBarca = ColumnDataSource(data=dict(
        partidos = dataBarca["partidos"],
        goles = dataBarca["goles"],
        paradas = dataBarca["paradas"],
        asistencias = dataBarca["asistencias"],
        edad = dataBarca["edad"],
        numero = dataBarca["numero"],
        
        x=dataBarca[xp],
        y=dataBarca[yp],
        nombre=dataBarca.nombre,
        posicion = dataBarca.posicion,
        nacionalidad = dataBarca.nacionalidad

    ))

    
    ############## Real Madrid ################################
sourceRealMadrid = ColumnDataSource(data=dict(
        partidos = dataRealMadrid["partidos"],
        goles = dataRealMadrid["goles"],
        paradas = dataRealMadrid["paradas"],
        asistencias = dataRealMadrid["asistencias"],
        edad = dataRealMadrid["edad"],
        numero = dataRealMadrid["numero"],


        x=dataRealMadrid[xp],
        y=dataRealMadrid[yp],
        nombre=dataRealMadrid.nombre,
        posicion = dataRealMadrid.posicion,
        nacionalidad = dataRealMadrid.nacionalidad

    ))

    
    ############## Athletic Club ################################
sourceAthleticClub = ColumnDataSource(data=dict(
        partidos = dataAthleticClub["partidos"],
        goles = dataAthleticClub["goles"],
        paradas = dataAthleticClub["paradas"],
        asistencias = dataAthleticClub["asistencias"],
        edad = dataAthleticClub["edad"],
        numero = dataAthleticClub["numero"],
        
        x=dataAthleticClub[xp],
        y=dataAthleticClub[yp],
        nombre=dataAthleticClub.nombre,
        posicion = dataAthleticClub.posicion,
        nacionalidad = dataAthleticClub.nacionalidad

    ))
    ##################################################################



    
    
