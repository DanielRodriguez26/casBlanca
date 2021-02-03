import mysql.connector
import datetime
import modules.customhash as customhash
import modules.globalvariables as gb
from flask import request,render_template,url_for, session

globalvariables = gb.GlobalVariables(True)
mydb= mysql.connector.connect(
    host=globalvariables.MysqlHost,
    user=globalvariables.MysqlUser,
    password=globalvariables.MysqlPassword,
    database=globalvariables.MysqlDatabase)  

class authenticateResponse:
    # URL a la que va a ser redirigido el usuario. Puede ser el home de un usuario especifico en caso de que la autenticación sea exitosa, o al mismo formulario
    # de login en caso contrario
    url = ""
    # Algunos formularios de home de usuario requieren que se les envíe el id
    id = 0
    # Algunos formularios requieren que la URL no sea un render_template, sino un redirect. En estos casos se usa redirect en True
    redirect = False
    #Campo para almacenar dinámicante el mensaje de bloque de la tabla Bloqueos.
    mensaje = ""

    isValid = True
    # Determina si el usuario está siendo usado en otro dispositivo
    secondDevice = 0


def authenticate(id, contra):
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuarios WHERE username=%s", (id,))
    user = cur.fetchone()
    cur.close()
    response = authenticateResponse()
    if user != None:
        hashedPass = customhash.hash(contra)
        contrasenia = user["passwordUsuario"]
        if contrasenia  == hashedPass:
            response.isValid = True

            session["rol"] = user["rol"]

            if user["rol"] == 1:
                session["adminSuper"] = id
                response.redirect = True
                response.url = url_for("home")
                return response
            if user["rol"] == 2:
                session["admin"] = id
                response.redirect = True
                response.url = url_for('home')
                return response
            if user["rol"] == 3:
                session["ventas"] = id
                response.redirect = True
                response.url = url_for('homeVentas')
                return response
        else:
            response.redirect = False
    else:
        response.redirect = False