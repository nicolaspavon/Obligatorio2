import json
import requests

def detallesPelis(nombre):
    nombrePeli=nombre.split(" ")
    direccion=str(nombrePeli[0])
    for i in range(len(nombrePeli)-1):
        direccion=direccion+"%20"+nombrePeli[i+1]
    data= requests.get("http://www.omdbapi.com/?apikey=a2d2e50e&t="+direccion)
    dicc=json.load(data)
    
