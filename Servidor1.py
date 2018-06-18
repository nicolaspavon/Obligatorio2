import cgi, cgitb
cgitb.enable() # Nos permite ver errores

pagina = open(r"prueba.txt")
for linea in pagina:
    print(linea)
pagina.close()
