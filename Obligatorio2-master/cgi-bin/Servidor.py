import cgitb
cgitb.enable() # Nos permite ver errores

pagina = open(r"C:\Users\estudiante.fit\Desktop\Obligatorio\prueba.txt")
for linea in pagina:
    print(linea)
pagina.close()
