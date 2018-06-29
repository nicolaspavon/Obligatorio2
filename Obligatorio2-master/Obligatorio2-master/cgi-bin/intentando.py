from datetime import date, timedelta
import cargar
def cargarHtml():
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
        print(TablasHtml())
    ("""</tbody></table>
    </body>
    </html>""")

