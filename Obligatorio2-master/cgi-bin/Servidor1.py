import cgi, cgitb
import intentando
cgitb.enable() # Nos permite ver errores

intentando.cargarHtml()
html = r"arch.txt"
pagina = open(html)
for linea in pagina:
    print(linea)
pagina.close()
