from datetime import date, timedelta
import cargar
def cargarHtml():
    print("GENERANDO HTML")
    arch=open("cgi-data/arch.txt","w")
    arch.write("""<html>
     <head>
      <title>CINES LTDA</title>
     </head>
     <body>
      <h1 style="text-align:center;">
      CINES Ltda </h1>
      <p>Catelera</p>
       <table style="text-align: left; margin-left: auto; margin-right: auto;" width="100%" cellpadding="0" cellspacing="0">
        <tbody>""")

    listaActual=cargar.CarteleraActual()
    lista=[]
    for posicion in range(len(listaActual)):
        dicc=cargar.DatosPelicula(listaActual[posicion])
        if posicion%3 == 0:
            arch.write("<tr><td><img src="+dicc["Poster"]+"/></td>")
            lista.append(dicc["Title"])
        elif posicion%3 == 1:
            arch.write("<td><img src="+dicc["Poster"]+"/></td>")
            lista.append(dicc["Title"])
        else:
            arch.write("<td><img src="+dicc["Poster"]+"/></td></tr>")
            lista.append(dicc["Title"])
        if (posicion%3==0 and posicion/3>=1) or (posicion==len(listaActual)-1):
            for elemento in lista:
                if posicion%3 == 0:
                    arch.write("""<tr><td align="center">"""+dicc["Title"]+"/></td>")
                elif posicion%3 == 1:
                    arch.write("""<td align="center">"""+dicc["Title"]+"/></td>")
                else:
                    arch.write("""<td align="center">"""+dicc["Title"]+"/></td></tr>")


    arch.write("""</tbody></table>
    </body>
    </html>""")
    arch.close()
