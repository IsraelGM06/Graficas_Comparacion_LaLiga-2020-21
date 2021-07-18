from bokeh.layouts import row
import pandas as pd
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.io import output_file, show
import data
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import CustomJS, Select

output_file("Comparación LaLiga 2020-21.html", title="Comparación LaLiga 2020/21")
# Con esta función damos los datos del archivo html que bokeh.show retorna, en este caso el nombre del archivo html
# Y el titulo en la pestaña de la página



TOOLTIPS = [
    ("X", "@x"),
    ("Y", "@y"),
    ("Nombre", "@nombre"),
    ("Edad", "@edad"),
    ("Posicion", "@posicion"),
    ("Nacionalidad","@nacionalidad")
]
    
# Este "array" sirve para saber que datos mostrar cuando el cursor esta encima de algún punto

###################################################################################

p = figure(title="LaLiga 20/21",tools = "pan,wheel_zoom,hover,reset",tooltips=TOOLTIPS,plot_width=600, plot_height=600)

# Creamos una figura, le damos un titulo, y "tools" son las herramientas que podemos tener en la barra de herramientas del costado de la figura
# también le podemos dar las medidas

equipos = ["Barca","Athletic Club","Real Madrid","Atletico de Madrid"]

# Este "array" nos ayuda a hacer el "for loop" para empezar a crear los puntos y para hacer las leyendas

for i, b in enumerate(equipos):
# "enumerate" nos retorna 2 valores del "array" que le demos por parámetro, el índice(i) de cada elemento y el valor de este índice (b)
    if(i == 0):
        source = data.sourceBarca
        # A cada vuelta cambiamos la variable "source" que esta en el archivo "data.py"
        color = "#5E0044"
        # También cambiamos la variable "color" por un color representativo de cada club
    if(i == 1):
        source = data.sourceAthleticClub
        color ="#000000"
    if(i == 2):
        source  = data.sourceRealMadrid
        color = "#EFB810"
    if(i == 3):
        source=data.sourceAtleticoMadrid
        color = "#DB3524"
    p.circle('x', 'y', color = color, source = source, legend_label = b,fill_alpha=0.7, size=9)
    # Dentro del "loop" creamos los círculos con los datos de la variable "source" y los ponemos del color que indique
    # la variable "color", a su vez agregamos el "legend_label" correspondiente a cada grupo de círculos que es dado por
    # la variable "b", también podemos poner diferentes características que queremos que tengan los puntos, como el tamaño
    # "size" y la transparencia "fill_alpha"

    
p.legend.click_policy = 'hide'
# Agregamos esta línea para que cuando se presiona alguna leyenda se oculten o aparezcan los círculos de esta leyenda
p.xaxis.axis_label = "X"
p.yaxis.axis_label = "Y"

xp="partidos"
yp="goles"

# Estas variables son los valores de x / y que se evalúan al iniciar
    
############################### SELECT ###########################
option=["partidos", "goles", "paradas","asistencias","edad","numero"]
# En este "array" damos todas las opciones de valores a comparar
selectx = Select(title="Select X:", value=xp, options=option,)
selecty = Select(title="Select Y:", value=yp, options=option)
# Creamos las barras de seleccionar y como valores de inicio damos las variables "xp" y "yp" y también las opciones que deben mostrar

callbackx = CustomJS(args=dict(p=p,
# Este "callback" va a servir para cambiar los valores de X / Y en cada "source" según el valor de las barras "select"
sourceBarca = data.sourceBarca,sourceAthleticClub=data.sourceAthleticClub,sourceAtleticoMadrid=data.sourceAtleticoMadrid,sourceRealMadrid=data.sourceRealMadrid,
# Dentro del diccionario de CustomJS inicializa todos los "source" o la data de cada club
select=selectx), code=
    """
    // Esta parte se tiene que escribir en JavaScript al ejecutarse en una página web
    var value = cb_obj.value.toString();
    // La variable "value" guarda el valor que se escoja en el selector de X

    const new_Barca = Object.assign({}, sourceBarca.data)
    // Se crea una "ColumnDataSource" provisional exactamente igual los datos principales
    new_Barca.x = sourceBarca.data[value]
    // Es esta variable provisional cambia la variable de X por los datos de el valor elegido en el "source" inicial
    sourceBarca.data = new_Barca
    // Y con la variable X con los datos nuevos se iguala al "source" inicial

    // Esto se repite con las variable X de el "source" de todos los equipos
    // Y para el “callback” Y casi igual, la única diferencia es que se cambia la variable Y de cada "source"

    const new_AthleticClub = Object.assign({}, sourceAthleticClub.data)
    new_AthleticClub.x = sourceAthleticClub.data[value]
    sourceAthleticClub.data = new_AthleticClub
   
    const new_AtleticoMadrid = Object.assign({}, sourceAtleticoMadrid.data)
    new_AtleticoMadrid.x = sourceAtleticoMadrid.data[value]
    sourceAtleticoMadrid.data = new_AtleticoMadrid

    const new_RealMadrid = Object.assign({}, sourceRealMadrid.data)
    new_RealMadrid.x = sourceRealMadrid.data[value]
    sourceRealMadrid.data = new_RealMadrid
    
    """
    )
callbacky = CustomJS(args=dict(p=p,
sourceBarca = data.sourceBarca,sourceAthleticClub=data.sourceAthleticClub,sourceAtleticoMadrid=data.sourceAtleticoMadrid,sourceRealMadrid=data.sourceRealMadrid,
select=selecty), code=
    """
    var value = cb_obj.value.toString();

    const new_Barca = Object.assign({}, sourceBarca.data)
    new_Barca.y = sourceBarca.data[value]
    sourceBarca.data = new_Barca

    const new_AthleticClub = Object.assign({}, sourceAthleticClub.data)
    new_AthleticClub.y = sourceAthleticClub.data[value]
    sourceAthleticClub.data = new_AthleticClub
   
    const new_AtleticoMadrid = Object.assign({}, sourceAtleticoMadrid.data)
    new_AtleticoMadrid.y = sourceAtleticoMadrid.data[value]
    sourceAtleticoMadrid.data = new_AtleticoMadrid

    const new_RealMadrid = Object.assign({}, sourceRealMadrid.data)
    new_RealMadrid.y = sourceRealMadrid.data[value]
    sourceRealMadrid.data = new_RealMadrid
   
    
    """
    )
    
    
          
selectx.js_on_change("value", callbackx)
# Esta función ejecutara el "callback" cada vez que haya un cambio en el selector
selecty.js_on_change("value", callbacky)
    
###############################################################

option=row(selectx,selecty)
# Agrupamos los 2 selectores en una fila
# Después esta fila la agrupamos con la figura del gráfico en una columna
show(column(option,p))