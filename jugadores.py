"""
Toda la información de los jugadores esta agrupada en diccionarios de cada equipo, cada equipo tiene un código que es la "key"
de un diccionario con los datos de los diferentes jugadores

Los datos de un portero y el resto de jugadores no son los mismos, los datos de un portero son, nombre, edad, numero, partidos,
paradas, nacionalidad, posición. Mientras que los datos de el resto de los jugadores son, nombre, edad, numero, partidos,
goles, asistencias, nacionalidad, posición.

Todos los datos fueron sacados de las paginas oficiales de cada club y de la pagina oficial de “LaLiga”

"""

jugadoresBarca={
        "JB1":{
            "nombre":"Marc-André ter Stegen",
            "edad":29,
            "numero":1,
            "partidos":31,
            "paradas":78,
            "nacionalidad":"Alemania",
            "posicion":"POR",
        },
        "JB2":{
            "nombre":"Neto Murara",
            "edad":31,
            "numero":13,
            "partidos":7,
            "paradas":18,
            "nacionalidad":"Brazil",
            "posicion":"POR",
        },
        "JB3":{
            "nombre":"Sergiño Dest",
            "edad":20,
            "numero":2,
            "partidos": 30,
            "goles": 2,
            "asistencias": 1,
            "nacionalidad":"USA",
            "posicion":"DEF",
        },
        "JB4":{
            "nombre":"Gerard Piqué",
            "edad":34,
            "numero":3,
            "partidos":18,
            "goles":0,
            "asistencias":0,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
        "JB5":{
            "nombre":"Ronald Araújo",
            "edad":22,
            "numero":4,
            "partidos":24,
            "goles":2,
            "asistencias":1,
            "nacionalidad":"Uruguay",
            "posicion":"DEF",
        },
        "JB6":{
            "nombre":"Clément Lenglet",
            "edad":26,
            "numero":15,
            "partidos":33,
            "goles":1,
            "asistencias":0,
            "nacionalidad":"Francia",
            "posicion":"DEF",
        },
        "JB7":{
            "nombre":"Jordi Alba",
            "edad":32,
            "numero":18,
            "partidos":35,
            "goles":3,
            "asistencias":5,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
        "JB8":{
            "nombre":"Sergi Roberto",
            "edad":29,
            "numero":20,
            "partidos":15,
            "goles":1,
            "asistencias":2,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
        "JB9":{
            "nombre":"Samuel Umtiti",
            "edad":27,
            "numero":23,
            "partidos":13,
            "goles":0,
            "asistencias":0,
            "nacionalidad":"Francia",
            "posicion":"DEF",
        },
        "JB10":{
            "nombre":"Junior Firpo",
            "edad":24,
            "numero":24,
            "partidos":7,
            "goles":1,
            "asistencias":1,
            "nacionalidad":"Español",
            "posicion":"DEF",
        },
        "JB11":{
            "nombre":"Sergio Busquets",
            "edad":33,
            "numero":5,
            "partidos":36,
            "goles":0,
            "asistencias":5,
            "nacionalidad":"España",
            "posicion":"MED",
        },
        "JB12":{
            "nombre":"Miralem Pjanić",
            "edad":31,
            "numero":8,
            "partidos":19,
            "goles":0,
            "asistencias":0,
            "nacionalidad":"Bosnia y Herzegovina",
            "posicion":"MED",
        },
        "JB13":{
            "nombre":"Riqui Puig",
            "edad":21,
            "numero":12,
            "partidos":14,
            "goles":1,
            "asistencias":0,
            "nacionalidad":"España",
            "posicion":"MED",
        },
        "JB14":{
            "nombre":"Philippe Coutinho",
            "edad":28,
            "numero":14,
            "partidos":12,
            "goles":2,
            "asistencias":2,
            "nacionalidad":"Brazil",
            "posicion":"MED",
        },
        "JB15":{
            "nombre":"Pedri González",
            "edad":18,
            "numero":16,
            "partidos":37,
            "goles":3,
            "asistencias":3,
            "nacionalidad":"España",
            "posicion":"MED",
        },
        "JB16":{
            "nombre":"Matheus Fernandes",
            "edad":22,
            "numero":19,
            "partidos":1,
            "goles":0,
            "asistencias":0,
            "nacionalidad":"Brazil",
            "posicion":"MED",
        },
        "JB17":{
            "nombre":"Frenkie de Jong",
            "edad":24,
            "numero":21,
            "partidos":37,
            "goles":3,
            "asistencias":4,
            "nacionalidad":"Píses Bajos",
            "posicion":"MED",
        },
        "JB18":{
            "nombre":"Antoine Griezmann",
            "edad":30,
            "numero":7,
            "partidos":36,
            "goles":13,
            "asistencias":7,
            "nacionalidad":"Francia",
            "posicion":"DEL",
        },
        "JB19":{
            "nombre":"Martin Braithwaite",
            "edad":30,
            "numero":9,
            "partidos":29,
            "goles":2,
            "asistencias":2,
            "nacionalidad":"Dinamarca",
            "posicion":"DEL",
        },
        "JB20":{
            "nombre":"Lionel Messi",
            "edad":34,
            "numero":10,
            "partidos":35,
            "goles":30,
            "asistencias":9,
            "nacionalidad":"Argentina",
            "posicion":"DEL",
        },
        "JB21":{
            "nombre":"Ousmane Dembélé",
            "edad":24,
            "numero":11,
            "partidos":30,
            "goles":6,
            "asistencias":2,
            "nacionalidad":"Francia",
            "posicion":"DEL",
        },
        "JB22":{
            "nombre":"Francisco Trincão",
            "edad":21,
            "numero":17,
            "partidos":28,
            "goles":3,
            "asistencias":2,
            "nacionalidad":"Portugal",
            "posicion":"DEL",
        },
        "JB23":{
            "nombre":"Ansu Fati",
            "edad":18,
            "numero":22,
            "partidos":7,
            "goles":4,
            "asistencias":0,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    
}
jugadoresRealMadrid={
        "JRM1":{
            "nombre":"Thibaut Courtois",
            "edad":29,
            "numero":1,
            "partidos":38,
            "paradas":90,
            "nacionalidad":"Bélgica",
            "posicion":"POR",
        },
        "JRM2":{
            "nombre":"Andriy Lunin",
            "edad":22,
            "numero":13,
            "partidos":0,
            "paradas":0,
            "nacionalidad":"Ucrania",
            "posicion":"POR",
        },
        "JRM3":{
            "nombre":"Dani Carvajal",
            "edad":29,
            "numero":2,
            "partidos": 13,
            "goles": 0,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
        "JRM4":{
            "nombre":"Éder Militão",
            "edad":23,
            "numero":3,
            "partidos": 14,
            "goles": 1,
            "asistencias": 0,
            "nacionalidad":"Brazil",
            "posicion":"DEF",
        },
         "JRM5":{
            "nombre":"Sergio Ramos",
            "edad":35,
            "numero":4,
            "partidos": 15,
            "goles": 2,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
        "JRM6":{
            "nombre":"Raphaël Varane",
            "edad":28,
            "numero":5,
            "partidos": 31,
            "goles": 2,
            "asistencias": 0,
            "nacionalidad":"Francia",
            "posicion":"DEF",
        },
        "JRM7":{
            "nombre":"Nacho Fernández",
            "edad":31,
            "numero":6,
            "partidos": 24,
            "goles": 1,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
        "JRM8":{
            "nombre":"Marcelo Vieira",
            "edad":33,
            "numero":12,
            "partidos": 16,
            "goles": 0,
            "asistencias": 2,
            "nacionalidad":"Brazil",
            "posicion":"DEF",
        },
        "JRM9":{
            "nombre":"Álvaro Odriozola",
            "edad":25,
            "numero":19,
            "partidos": 13,
            "goles": 2,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
        "JRM10":{
            "nombre":"Ferland Mendy",
            "edad":25,
            "numero":23,
            "partidos": 26,
            "goles": 1,
            "asistencias": 0,
            "nacionalidad":"Francia",
            "posicion":"DEF",
        },
        "JRM11":{
            "nombre":"Toni Kroos",
            "edad":31,
            "numero":8,
            "partidos": 28,
            "goles": 3,
            "asistencias": 10,
            "nacionalidad":"Alemania",
            "posicion":"MED",
        },
        "JRM12":{
            "nombre":"Luka Modrić",
            "edad":35,
            "numero":10,
            "partidos": 35,
            "goles": 5,
            "asistencias": 3,
            "nacionalidad":"Croacia",
            "posicion":"MED",
        },
        "JRM13":{
            "nombre":"Carlos Casemiro",
            "edad":29,
            "numero":14,
            "partidos": 34,
            "goles": 6,
            "asistencias": 4,
            "nacionalidad":"Brazil",
            "posicion":"MED",
        },
        "JRM14":{
            "nombre":"Fede Valverde",
            "edad":22,
            "numero":15,
            "partidos": 24,
            "goles": 3,	
            "asistencias": 1,
            "nacionalidad":"Uruguay",
            "posicion":"MED",
        },
        "JRM15":{
            "nombre":"Isco Alarcón",
            "edad":29,
            "numero":22,
            "partidos": 25,
            "goles": 0,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"MED",
        },
        "JRM16":{
            "nombre":"Eden Hazard",
            "edad":30,
            "numero":7,
            "partidos": 14,
            "goles": 3,
            "asistencias": 2,
            "nacionalidad":"Bélgica",
            "posicion":"DEL",
        },
        "JRM17":{
            "nombre":"Karim Benzema",
            "edad":33,
            "numero":9,
            "partidos": 34,
            "goles": 23,
            "asistencias": 9,
            "nacionalidad":"Francia",
            "posicion":"DEL",
        },
        "JRM18":{
            "nombre":"Marco Asensio",
            "edad":25,
            "numero":11,
            "partidos": 35,
            "goles": 5,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
        "JRM19":{
            "nombre":"Lucas Vázquez",
            "edad":29,
            "numero":17,
            "partidos": 24,
            "goles": 2,
            "asistencias": 5,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
        "JRM20":{
            "nombre":"Vinícius Júnior",
            "edad":21,
            "numero":20,
            "partidos": 35,
            "goles": 3,
            "asistencias": 3,
            "nacionalidad":"Brazil",
            "posicion":"DEL",
        },
        "JRM21":{
            "nombre":"Mariano Díaz",
            "edad":27,
            "numero":24,
            "partidos": 16,
            "goles": 1,
            "asistencias": 0,
            "nacionalidad":"Español",
            "posicion":"DEL",
        },
        "JRM22":{
            "nombre":"Rodrygo Goes",
            "edad":20,
            "numero":25,
            "partidos": 22,
            "goles": 1,	
            "asistencias": 6,
            "nacionalidad":"Brazil",
            "posicion":"DEL",
        },
    
}
jugadoresAtleticoMadrid={
    "JAM1":{
            "nombre":"Ivo Grbić",
            "edad":25,
            "numero":1,
            "partidos":0,
            "paradas":0,
            "nacionalidad":"Croacia",
            "posicion":"POR",
        },
    "JAM2":{
            "nombre":"Jan Oblak",
            "edad":28,
            "numero":13,
            "partidos":38,
            "paradas":103,
            "nacionalidad":"Eslovenia",
            "posicion":"POR",
        },
    "JAM3":{
            "nombre":"José María Giménez",
            "edad":26,
            "numero":2,
            "partidos": 21,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"Uruguay",
            "posicion":"DEF",
        },
    "JAM4":{
            "nombre":"Renan Lodi",
            "edad":23,
            "numero":12,
            "partidos": 23,
            "goles": 1,
            "asistencias": 2,
            "nacionalidad":"Brazil",
            "posicion":"DEF",
        },
    "JAM5":{
            "nombre":"Stefan Savić",
            "edad":30,
            "numero":15,
            "partidos": 33,
            "goles": 1,
            "asistencias": 0,
            "nacionalidad":"Montenegro",
            "posicion":"DEF",
        },
    "JAM6":{
            "nombre":"Felipe Augusto",
            "edad":32,
            "numero":18,
            "partidos": 31,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"Brazil",
            "posicion":"DEF",
        },
    "JAM7":{
            "nombre":"Mario Hermoso",
            "edad":26,
            "numero":22,
            "partidos": 31,
            "goles": 1,
            "asistencias":1,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAM8":{
            "nombre":"Kieran Trippier",
            "edad":30,
            "numero":23,
            "partidos":28,
            "goles": 0,
            "asistencias": 6,
            "nacionalidad":"Inglaterra",
            "posicion":"DEF",
        },
    "JAM9":{
            "nombre":"Šime Vrsaljko",
            "edad":29,
            "numero":24,
            "partidos": 9,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"Croacia",
            "posicion":"DEF",
        },
    "JAM10":{
            "nombre":"Geoffrey Kondogbia",
            "edad":28,
            "numero":4,
            "partidos": 25,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"República Centroafricana",
            "posicion":"MED",
        },
    "JAM11":{
            "nombre":"Lucas Torreira",
            "edad":25,
            "numero":5,
            "partidos": 19,
            "goles": 1,
            "asistencias":0,
            "nacionalidad":"Uruguay",
            "posicion":"MED",
        },
    "JAM12":{
            "nombre":"Koke Resurrección",
            "edad":29,
            "numero":6,
            "partidos":37,
            "goles": 1,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAM13":{
            "nombre":"Saúl Ñíguez",
            "edad":26,
            "numero":8,
            "partidos": 33,
            "goles": 2,
            "asistencias": 1,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAM14":{
            "nombre":"Thomas Lemar",
            "edad":25,
            "numero":11,
            "partidos": 27,
            "goles": 1,
            "asistencias": 3,
            "nacionalidad":"Francia",
            "posicion":"MED",
        },
    "JAM15":{
            "nombre":"Marcos Llorente",
            "edad":26,
            "numero":14,
            "partidos": 37,
            "goles": 12,
            "asistencias": 11,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAM16":{
            "nombre":"Héctor Herrera",
            "edad":31,
            "numero":16,
            "partidos": 16,
            "goles": 0,
            "asistencias": 1,
            "nacionalidad":"México",
            "posicion":"MED",
        },
    "JAM17":{
            "nombre":"Vitolo Machín",
            "edad":31,
            "numero":20,
            "partidos":10,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAM18":{
            "nombre":"Yannick Carrasco",
            "edad":27,
            "numero":21,
            "partidos": 30,
            "goles": 6,
            "asistencias": 10,
            "nacionalidad":"Bélgica",
            "posicion":"MED",
        },
    "JAM19":{
            "nombre":"João Félix",
            "edad":21,
            "numero":7,
            "partidos": 31,
            "goles": 7,
            "asistencias": 5,
            "nacionalidad":"Portugal",
            "posicion":"DEL",
        },
    "JAM20":{
            "nombre":"Luis Suárez",
            "edad":34,
            "numero":9,
            "partidos": 32,
            "goles": 21,
            "asistencias": 3,
            "nacionalidad":"Uruguay",
            "posicion":"DEL",
        },
    "JAM21":{
            "nombre":"Ángel Correa",
            "edad":26,
            "numero":10,
            "partidos":38,
            "goles": 9,
            "asistencias": 8,
            "nacionalidad":"Argentina",
            "posicion":"DEL",
        },
    "JAM22":{
            "nombre":"Moussa Dembélé",
            "edad":24,
            "numero":19,
            "partidos": 5,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"Francia",
            "posicion":"DEL",
        },
}

jugadoresAthleticClub={
    "JAC1":{
            "nombre":"Unai Simón",
            "edad":23,
            "numero":1,
            "partidos":37,
            "paradas":70,
            "nacionalidad":"España",
            "posicion":"POR",
        },
    "JAC2":{
            "nombre":"Jokin Ezkieta",
            "edad":24,
            "numero":13,
            "partidos":1,
            "paradas":1,
            "nacionalidad":"España",
            "posicion":"POR",
        },
    
    "JAC3":{
            "nombre":"Unai Núñez",
            "edad":24,
            "numero":3,
            "partidos": 25,
            "goles": 1,
            "asistencias": 1,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC4":{
            "nombre":"Iñigo Martínez",
            "edad":30,
            "numero":4,
            "partidos": 28,
            "goles": 1,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC5":{
            "nombre":"Yeray Álvarez",
            "edad":26,
            "numero":5,
            "partidos": 23,
            "goles": 1,
            "asistencias": 0 ,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC6":{
            "nombre":"Iñigo Lekue",
            "edad":28,
            "numero":15,
            "partidos": 18,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC7":{
            "nombre":"Yuri Berchiche",
            "edad":31,
            "numero":16,
            "partidos": 23,
            "goles": 1,
            "asistencias": 3,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC8":{
            "nombre":"Óscar de Marcos",
            "edad":32,
            "numero":18,
            "partidos": 25,
            "goles": 1,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC9":{
            "nombre":"Ander Capa",
            "edad":29,
            "numero":21,
            "partidos": 28,
            "goles": 2,
            "asistencias": 1,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC10":{
            "nombre":"Peru Nolaskoain",
            "edad":22,
            "numero":23,
            "partidos": 0,
            "goles": 2,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC11":{
            "nombre":"Mikel Balenziaga",
            "edad":33,
            "numero":24,
            "partidos": 23,
            "goles": 0,
            "asistencias": 1,
            "nacionalidad":"España",
            "posicion":"DEF",
        },
    "JAC12":{
            "nombre":"Mikel Vesga",
            "edad":28,
            "numero":6,
            "partidos": 30,
            "goles": 0,
            "asistencias": 1,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAC13":{
            "nombre":"Unai López",
            "edad":25,
            "numero":8,
            "partidos": 26,
            "goles": 3,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAC14":{
            "nombre":"Dani García",
            "edad":31,
            "numero":14,
            "partidos": 27,
            "goles": 0,
            "asistencias":1,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAC15":{
            "nombre":"Oihan Sancet",
            "edad":21,
            "numero":16,
            "partidos": 24,
            "goles": 2,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAC16":{
            "nombre":"Oier Zarraga",
            "edad":22,
            "numero":19,
            "partidos":5 ,
            "goles": 0,
            "asistencias":0 ,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAC17":{
            "nombre":"Unai Vencedor",
            "edad":20,
            "numero":27,
            "partidos":28 ,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"MED",
        },
    "JAC18":{
            "nombre":"Jon Morcillo",
            "edad":22,
            "numero":2,
            "partidos":30,
            "goles": 2,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    "JAC19":{
            "nombre":"Ibai Gómez",
            "edad":31,
            "numero":7,
            "partidos":13,
            "goles": 0,
            "asistencias": 1,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    "JAC20":{
            "nombre":"Iñaki Williams",
            "edad":27,
            "numero":9,
            "partidos":38,
            "goles": 6,
            "asistencias": 6,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    "JAC21":{
            "nombre":"Álex Berenguer",
            "edad":26,
            "numero":12,
            "partidos":35,
            "goles": 8,
            "asistencias": 4,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    "JAC22":{
            "nombre":"Iker Muniain",
            "edad":28,
            "numero":10,
            "partidos":28,
            "goles": 5,
            "asistencias": 3,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    "JAC23":{
            "nombre":"Asier Villalibre",
            "edad":23,
            "numero":20,
            "partidos":35,
            "goles": 4,
            "asistencias": 2,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    "JAC24":{
            "nombre":"Raúl García",
            "edad":34,
            "numero":22,
            "partidos":34,
            "goles": 5,
            "asistencias": 1,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
    "JAC25":{
            "nombre":"Iñigo Vicente",
            "edad":23,
            "numero":26,
            "partidos":3,
            "goles": 0,
            "asistencias": 0,
            "nacionalidad":"España",
            "posicion":"DEL",
        },
}