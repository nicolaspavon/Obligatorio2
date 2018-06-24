from datetime import date, timedelta

print("""<html>
 <head>
  <title>CINES LTDA</title>
 </head>
 <body>
  <h1 style="text-align:center;">
  CINES Ltda </h1>
  <p>Catelera</p>
   <table style="text-align: left; margin-left: auto; margin-right: auto;" width="100%" cellpadding="0" cellspacing="0">
    <tbody>""")

listaActual=CartelerActual()
lista=[]
for posicion in range(len(listaActual)):
    dicc=DatosPelicula(imbdID)
    if posicion%3 == 0:
        print("<tr><td><img src="+dicc.pop("Poster")+"/></td>")
        lista.append(dicc.pop("Title"))
    elif posicion%3 == 1:
        print("<td><img src="+dicc.pop("Poster")+"/></td>")
        lista.append(dicc.pop("Title"))
    else:
        print("<td><img src="+dicc.pop("Poster")+"/></td></tr>")
        lista.append(dicc.pop("Title"))
    if (posicion%3==0 and posicion/3>=1) or (posicion==len(listaActual)-1)):
        for elemento in lista:
            if posicion%3 == 0:
                print("<tr><td align="center">"+dicc.pop("Title")+"/></td>")
            elif posicion%3 == 1:
                print("<td align="center">"+dicc.pop("Title")+"/></td>")
            else:
                print("<td align="center">"+dicc.pop("Title")+"/></td></tr>")


print("""</tbody></table>
</body>
</html>""")
