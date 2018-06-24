import json
import requests
from datetime import date, timedelta


#Con esta funcion se crea un diccionario a partir de los datos que brinda la pagina OMDB
def detallesPelis(nombre):
    
    nombrePeli = nombre.split(" ")
    direccion = str(nombrePeli[0])
    for i in range(len(nombrePeli)-1):
        direccion = direccion+"%20"+nombrePeli[i+1]
    data = requests.get("http://www.omdbapi.com/?apikey=a2d2e50e&t="+direccion)
    dicc = json.load(data) #Se deserializan los datos convirtiendolos en diccionario
    return dicc


#Verificar si las fechas en cuestion esta dentro del rango de tiempo de la pelicula proyectada
def VerificarTiempo(fechaEstreno, fechaFin, fechaActual):
    
    fechaInicio = fechaEstreno.split("/")
    fechaFinal = fechaFin.split("/")
    fechaHoy = fechaActual.split("/")
    inicio = date(fechaInicio[2], fechaInicio[1], fechaInicio[0])
    fin = date(fechaFin[2], fechaFin[1], fechaFin[0])
    hoy = date(fechaActual[2], fechaActual[1], fechaActual[0])
    return hoy - inicio < fin - inicio
    

#Buscar si la pelicula consultada se esta proyectando en el cine y devolver numero de sala
def BuscarPeli(nombre):

    dicc = detallesPelis(nombre)
    numero = dicc.get("imdbID","Not found")
    nroSala = []
    hoy = date.today()
    if numero!="Not found":
        cartelera = open("carteleras.csv","r")
        for linea in cartelera:
            lineaSinError = linea.strip("\n")
            lista = lineaSinError.split(",")
            if lista[1] == numero:
                inicio = lista[2]
                fin = lista[3]
                if VerificarTiempo(inicio, fin,hoy)==True
                    nroSala.append(lista[1]) #Se agrega a la lista el Nro de Sala en el cual se proyecta la pelicula
        cartelera.close()
    return nroSala

#Datos de pelicula en salas
def DatosPelis(nroSala):
    
    salas = open("salas.csv","r")
    datos = ""
    for linea in salas:
        lineaSinError = linea.strip("\n")
        lista = lineaSinError.split(",")
        if nroSala == lista[0]:
            datos = datos + "El complejo en que que se proyecta es " + lista[1] + ", la direccion es " + lista[2] + "el telefono es " + lista[3] + "\n"
    salas.close()
    return datos
    #aca lo hice como que devuelva solo todo el texto , pero es ccuestion de modificar eso para que devuelva solo para un complejo y ta 

                       
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

        


    
