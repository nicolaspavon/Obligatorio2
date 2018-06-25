import cgi, cgitb
cgitb.enable() # Nos permite ver errores

html = r"prueba.txt"
pagina = open(html)
for linea in pagina:
    print(linea)
pagina.close()
