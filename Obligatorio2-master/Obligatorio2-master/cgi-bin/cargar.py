import json
import urllib.request
from datetime import date, timedelta

#Se utilizara para el buscador
#Con esta funcion se crea un diccionario a partir de los datos que brinda la pagina OMDB
def detallesPelis(nombre):
    
    nombrePeli = nombre.split(" ")
    direccion = str(nombrePeli[0])
    for i in range(len(nombrePeli)-1):
        direccion = direccion+"%20"+nombrePeli[i+1]
    data = urllib.request.urlopen("http://www.omdbapi.com/?apikey=a2d2e50e&t="+direccion)
    dicc = json.load(data) #Se deserializan los datos convirtiendolos en diccionario
    return dicc


#Verificar si las fechas en cuestion esta dentro del rango de tiempo de la pelicula proyectada
def VerificarTiempo(fechaEstreno, fechaFin, hoy):
    
    fechaInicio = fechaEstreno.split("/")
    fechaFinal = fechaFin.split("/")
    inicio = date(int(fechaInicio[2]), int(fechaInicio[1]), int(fechaInicio[0]))
    fin = date(int(fechaFinal[2]), int(fechaFinal[1]), int(fechaFinal[0]))
    return (inicio <= hoy ) and (hoy  <= fin )
    

#Buscar si la pelicula consultada se esta proyectando en el cine y devolver numero de sala
def BuscarPeli(nombre):

    dicc = detallesPelis(nombre)
    numero = dicc.get("imdbID","Not found")
    nroSala = []
    hoy = date.today()
    if numero!="Not found":
        cartelera = open("cgi-data/carteleras.csv","r")
        for linea in cartelera:
            lineaSinError = linea.strip("\n")
            lista = lineaSinError.split(",")
            if lista[1] == numero:
                inicio = lista[2]
                fin = lista[3]
                if VerificarTiempo(inicio, fin,hoy)==True:
                    nroSala.append(lista[1]) #Se agrega a la lista el Nro de Sala en el cual se proyecta la pelicula
        cartelera.close()
    return nroSala

#Datos de pelicula en salas
def DatosPelis(nroSala):
    
    salas = open("cgi-data/salas.csv","r")
    datos = ""
    if nroSala==[]:
        datos="La película no se encuentra en cartelera"
    else:
        for linea in salas:
            lineaSinError = linea.strip("\n")
            lista = lineaSinError.split(",")
            if nroSala == lista[0]:
                datos = datos + "El complejo en que que se proyecta es " + lista[1] + ", la direccion es " + lista[2] + "el telefono es " + lista[3] + "\n"
    salas.close()
    return datos
    #aca lo hice como que devuelva solo todo el texto , pero es ccuestion de modificar eso para que devuelva solo para un complejo y ta 


#Cartelera de peliculas del dia de hoy, por numero de imbdID
def CarteleraActual():

    hoy = date.today()
    peliculas = open("cgi-data/carteleras.csv","r")
    cartelera=[]
    for linea in peliculas:
        lineaSinError = linea.strip("\n")
        lista = lineaSinError.split(",")
        if VerificarTiempo(lista[2],lista[3],hoy) == True:
            cartelera.append(lista[1])
    return cartelera


#Datos de 1 pelicula en cartelera        
def DatosPelicula(imbdID):

    data = urllib.request.urlopen("http://www.omdbapi.com/?apikey=a2d2e50e&i="+imbdID)
    dicc = json.load(data) #Se deserializan los datos convirtiendolos en diccionario
    return dicc

#Datos de toda la cartelera a partir de numero de imbdID
def DatosCartelera(imbdIDLista):

    lista = []
    for imbdID in imbdIDLista:
        lista.append(DatosPelicula(imbdID))
    return lista

        
#Relacionando
def asignacion():
    
    lista = CarteleraActual()
    listaDeDicc = DatosCartelera(lista)
    return listaDeDicc

#Devolviendo lo que se precisa para la web, URL imagen y titulo
def ImagenTitulo(dicc):

    URL = dicc.get("Poster")
    Titulo = dicc.get("Title")
    return URL, Titutlo

#Cosas para el html
def TablasHtml():
    listaActual=cargar.CarteleraActual()
    lista=[]
    devolver=""
    for posicion in range(len(listaActual)):
        dicc=cargar.DatosPelicula(listaActual[posicion])
        if posicion%3 == 0:
            devolver = devolver +"<tr><td><img src="+dicc["Poster"]+"/></td> \n"
            lista.append(dicc["Title"])
        elif posicion%3 == 1:
            devolver = devolver +"<td><img src="+dicc["Poster"]+"/></td> \n"
            lista.append(dicc["Title"])
        else:
            devolver = devolver +"<td><img src="+dicc["Poster"]+"/></td></tr> \n"
            lista.append(dicc["Title"])
        if posicion == len(listaActual)-1 & (len(listaActual)-1)%==0:
            devolver = devolver + "</tr>+\n"
        if (posicion%3==0 and posicion/3>=1) or (posicion==len(listaActual)-1):
            for elemento in lista:
                if posicion%3 == 0:
                    devolver = devolver +"""<tr><td align="center">"""+dicc["Title"]+"/></td> \n"
                elif posicion%3 == 1:
                    devolver = devolver +"""<td align="center">"""+dicc["Title"]+"/></td> \n"
                else:
                    devolver = devolver +"""<td align="center">"""+dicc["Title"]+"/></td></tr> \n"
    return devolver


    
                       
###Lista de los nombres de peliculas que luego se cargaran a un archivo .csv
##NombrePelis=["Back to the future", "Titanic", "Freaky Friday", "Inception", "Midnight in Paris", "Irrational man", "Coco"]
##Capaz esos archivos ya tendria que estar creados
##
###Creacion de lista de diccionarios para todas las pelis
##def listaDeDicc(peliculas):
##    lista = []
##    for i in range (len(peliculas)):
##        lista.append(detallesPelis(peliculas[i]))
##    return lista
##

        


    
