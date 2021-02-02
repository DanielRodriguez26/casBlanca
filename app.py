import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g, make_response, session, escape, Response,json
import modules.authentication as authentication
from flask_mysqldb import MySQL
import modules.globalvariables as gb
import modules.customhash as customhash
import modules.usuarios as usuarios
import mysql.connector
import ast
import logging
import datetime



app = Flask(__name__)
mydb = None
logger = None
loggerAccess = None
globalvariables = None

def Initial():
    global app, mydb, logger
    try:
        #Configuración logger de errores
        logger = logging.getLogger('CasaBlanca')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        handler = logging.FileHandler('casaBlanca_error.log')
        handler.setLevel(logging.ERROR)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        globalvariables = gb.GlobalVariables(True)
        mydb= mysql.connector.connect(
            host=globalvariables.MysqlHost,
            user=globalvariables.MysqlUser,
            password=globalvariables.MysqlPassword,
            database=globalvariables.MysqlDatabase)  


        app.secret_key = "RGlCYW5rYTEuMCB3YXMgbWFkZSBmb3IgQ0FTVVIsIGFuZCB3cml0dGVuIGJ5IE1pZ3VlIGFuZCBEYW5pZWwuIEF0IHRoZSBlbmQgb2YgdGhlIHByb2plY3QsIEp1YW4sIEVkd2luLCBIdWdvIGFuZCBBbmRyw6lzIGpvaW5lZCB0aGUgdGVhbS4gTm93IHdlIGFyZSBhIGZpcmVmaWdodGVycyB0ZWFtLg=="
    except Exception as error:
        logger.exception(error)


def clearSession():
        # Para mas seguridad, al cargar la landingpage siempre se limpian todas las cookies
    session.clear()


Initial()
@app.route('/')
def login():
    try:
        clearSession()
        return render_template('login.html')
    except Exception as error:
            logger.exception(error)


@app.route('/loginVerify', methods=["GET", "POST"])
def loginVerify():
    try:
        if request.method == "POST":
            id = request.form['identificacion']
            contra = request.form['contraseña']
            session["username"] = id
            authenticateResponse = authentication.authenticate(id, contra)
            if (authenticateResponse.redirect):
                return redirect(authenticateResponse.url)
        else:
            return redirect("/")
    except Exception as error:
            logger.exception(error)

@app.route("/logout", methods=['POST','GET'])
def logout():
    try:
        Initial()
        if session:
            if session.get("SessionId"):
                sessionId = session["SessionId"]
                clearSession()

            return render_template('login.html')

    except Exception as error:
                logger.exception(error)


@app.route('/home')
def home():
    try:
        if "adminSuper" in session or "admin" in session: 
            
            return render_template('index.html')
        return render_template("403.html")
    except Exception as error:
            logger.exception(error)


# Productos
@app.route('/homeVentas')
def homeVentas():
    try:
        if "ventas" in session:             
                return render_template('indexVentas.html')
        return render_template("403.html")
    except Exception as error:
            logger.exception(error)


@app.route('/homePorductos')
def homePorductos():
    try:
        if "adminSuper" in session or "admin" in session or "ventas" in session:  
            cur = mydb.cursor(dictionary=True)
            cur.execute('''SELECT idProducto, nombreProducto ,precioProducto , fechaProducto FROM productos where cantidadProducto > 0''')
            productos = cur.fetchall()
            cur.close()
            productos = json.dumps(productos)        
            return render_template('homePorductos.html',productos=productos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/ingresoProductos')
def ingresoProductos():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur = mydb.cursor()
            cur.execute(''' SELECT idProducto, nombreProducto ,
                            precioProducto , fechaProducto,
                            cantidadProducto, valorUnidadProducto, 
                            valorTotalProducto,actualizarProducto,
                            totalDiaProducto
                            FROM productos''')
            productos = cur.fetchall()
            cur.close()
            return render_template('ingresoProductos.html',productos=productos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/salidaProductos')
def salidaProductos():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur = mydb.cursor()
            cur.execute('''SELECT idProducto, nombreProducto ,precioProducto , fechaProducto FROM productos ''')
            productos = cur.fetchall()
            cur.close()
            return render_template('salidaProductos.html',productos=productos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/cortecias')
def cortecias():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur = mydb.cursor(dictionary=True)
            cur.execute(''' SELECT nombreProducto ,precioProducto ,idProducto FROM productos where cantidadProducto > 0''')
            productos = cur.fetchall()
            cur.close()
            productos = json.dumps(productos)
            return render_template('cortecias.html',productos=productos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/facturaProducto',methods=['POST','GET'])
def facturaProducto():
    try:
        if "adminSuper" in session or "admin" in session or  "ventas" in session: 
            totalVenta = request.form['totalVenta']
            productos = request.form['productos']
            productos = ast.literal_eval(productos)
            idProducto = productos[0]
            contar = 0
            idDetalle=0
            id = session["username"] 
            cur = mydb.cursor()
            cur.execute(''' INSERT INTO facturas 
                            (totalFacturas,usuarioFactura,fechaFactura,estadoFactura) 
                            VALUES (%s,%s,now(),1)''',(totalVenta,id))            
            idFactura = cur.lastrowid

            for producto in productos:
                if idProducto == producto:
                    idProducto = producto
                    contar += 1 
                else: 
                    idProducto = producto
                    contar = 1


                if contar > 1:
                    cur.execute('''
                    UPDATE detalle SET cantidadDetalle = %s WHERE (idDetalle = %s)
                    ''', (contar,idDetalle,))

                    idDetalle =idDetalle 
                else:
                    cur.execute(''' INSERT INTO 
                                    detalle
                                    (idFacturaDetalle, idProductoDetalle, 
                                    cantidadDetalle, fechaDetalle) 
                                    VALUES (%s, %s, %s, now())''', 
                                    (idFactura,producto,contar))

                    idDetalle = cur.lastrowid
            mydb.commit()
            cur.close()
            return redirect(url_for('ingresoProductos'))
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)

# Usurios
@app.route('/usuarios')
def usuarios():    
    try:
        cur = mydb.cursor()
        cur.execute('''SELECT idUsuario,username,nombreUsuarios,apellidoUsuario,emailUsuario,rol,fechaUsuario FROM usuarios''')
        usuarios = cur.fetchall()
        cur.close()
        return render_template('usuarios.html',usuarios=usuarios)
    except Exception as error:
        logger.exception(error)


@app.route('/nuevoUsuario',methods=['POST','GET'])
def nuevoUsuario():
    try:
        if "adminSuper" in session or "admin" in session: 
        
            nombre=request.form['nombre']
            apellido=request.form['apellido']
            cedula=request.form['cedula']
            email=request.form['email']
            rol=request.form['rol']
            contraseña =request.form['contraseña']

            hashedPass = customhash.hash(contraseña)

            cur = mydb.cursor()

            cur.execute('''SELECT username FROM usuarios WHERE username=%s''',(cedula,))
            usuarios = cur.fetchone()
            if usuarios != None:
                mensaje = 'Esta cedula ya ya se encuentar agregada '
                return Response(json.dumps({'error': 'true','page': '/home', 'message':mensaje }),  mimetype='application/json')
            else:
                cur.execute(''' INSERT INTO 
                                usuarios 
                                (username, nombreUsuarios, 
                                apellidoUsuario,emailUsuario, 
                                passwordUsuario, rol, 
                                fechaUsuario)
                                VALUES (%s,%s,%s,%s,%s,%s,now()) ''',
                        (cedula, nombre, apellido, email,hashedPass, rol))
                mydb.commit()
            cur.close()
            return Response(json.dumps({'error': 'false','page': '/home' }),  mimetype='application/json')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/editarUsuario/<id>',methods=['POST','GET'])
def editarUsuario(id):
    try:
        if "adminSuper" in session or "admin" in session: 
            cur = mydb.cursor()
            cur.execute('''SELECT idUsuario,username,nombreUsuarios,apellidoUsuario,emailUsuario,rol,fechaUsuario FROM usuarios WHERE username=%s''',(id,))
            usuarios = cur.fetchall()
            cur.close()
            return render_template('editarUsuario.html',usuarios=usuarios)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/updateUsuario/<id>',methods=['POST','GET'])
def updateUsuario(id):
    try:
        if "adminSuper" in session or "admin" in session: 
            nombre=request.form['nombre']
            apellido=request.form['apellido']
            cedula=request.form['cedula']
            email=request.form['email']
            rol=request.form['rol']

            cur = mydb.cursor()
            
            cur.execute(''' UPDATE 
                            usuarios SET 
                            username = %s, 
                            nombreUsuarios = %s, 
                            apellidoUsuario = %s, 
                            emailUsuario = %s, 
                            rol = %s, 
                            fechaUsuario = now()
                            WHERE (username =%s)''',
                            (cedula,nombre, apellido, email, rol ,id))
            mydb.commit()
            cur.close()
            return Response(json.dumps({'error': 'false','page': '/usuarios' }),  mimetype='application/json')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/deleteUsuario/<id>', methods=['POST'])
def deleteUsuario(id):
    try:
        if "adminSuper" in session or "admin" in session: 
            cur =mydb.cursor()
            cur.execute('DELETE FROM usuarios WHERE username =%s',(id,))
            mydb.commit()
            cur.close()
            return redirect(url_for('home'))
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


# Detalles
@app.route('/detallesFactura',methods=['POST','GET'])
def detallesFactura():
    try:
        if "adminSuper" in session or "admin" in session or "ventas" in session: 
            cur = mydb.cursor()
            cur.execute('''SELECT idFactura,totalFacturas,fechaFactura,usuarioFactura,estadoFactura FROM facturas''')
            facturas = cur.fetchall()
            cur.close()
            return render_template('detalles.html',facturas=facturas)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/detallesProducto/<id>', methods=['POST','GET'])
def detallesProducto(id):
    try:
        if "adminSuper" in session or "admin" in session or "ventas" in session: 
            cur =mydb.cursor()
            cur.execute('''SELECT p.nombreProducto, p.precioProducto, 
                            d.cantidadDetalle, d.fechaDetalle, f.totalFacturas 
                            FROM detalle as d
                            inner join productos as p  on d.idProductoDetalle = p.idProducto
                            inner join facturas as f  on d.idFacturaDetalle = f.idFactura
                            where idFacturaDetalle = %s''',(id,))
            detalles = cur.fetchall()
            fechafac= detalles[0][3]
            totalPre= detalles[0][4]
            fechaHoy =datetime.date.today()
            cur.close()
            return render_template('detallesProductos.html',detalles=detalles,totalPre=totalPre,fechafac=fechafac,fechaHoy=fechaHoy)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


#Inventarios
@app.route('/nuevoProducto',methods=['POST','GET'])
def nuevoProducto():
    try:
        if "adminSuper" in session or "admin" in session: 
            nombreProducto=request.form['nombreProducto']
            precioProducto=request.form['precioProducto']
            cantidadNueva=request.form['cantidadNueva']
            valorNueva=request.form['valorNueva']
            valorT = valorNueva * cantidadNueva

            cur = mydb.cursor()

            cur.execute(''' INSERT INTO 
                            productos 
                            (nombreProducto, precioProducto, 
                            precioProducto,cantidadProducto, 
                            valorUnidadProducto, valorTotalProducto,fechaProducto)
                            VALUES (%s,%s,%s,%s,%s,%s,now()) ''',
                    (nombreProducto, precioProducto, cantidadNueva, valorNueva,valorT))
            mydb.commit()
            cur.close()
            return Response(json.dumps({'error': 'false','page': '/ingresoProductos' }),  mimetype='application/json')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)



@app.route('/editarCantidad',methods=['POST','GET'])
def editarCantidad():
    try:
        if "adminSuper" in session or "admin" in session or "ventas" in session: 
            idProducto=request.form['idProducto']
            cantidadNueva=request.form['cantidadNueva']
            valorNueva =request.form['valorNueva']
            cur =mydb.cursor()
            cur.execute('''SELECT cantidadProducto,valorTotalProducto  FROM productos WHERE  idProducto =%s ''',(idProducto,))
            productos = cur.fetchall()
            cantidadNueva=int(cantidadNueva)
            cantidadProducto = productos[0][0]
            CantidadT= cantidadProducto + cantidadNueva
            valorP = int(valorNueva) *cantidadNueva
            valorT= int(valorP) +productos[0][1]

            cur.execute(''' UPDATE productos 
                            SET cantidadProducto = %s, 
                            valorUnidadProducto = %s, 
                            valorTotalProducto = %s, 
                            fechaProducto =now()
                            WHERE (idProducto = %s);
                        ''', (CantidadT,valorNueva, valorT,idProducto) )
            productos = cur.fetchall()
                
            mydb.commit()
            cur.close()

            return Response(json.dumps({'error': 'false','page': '/ingresoProductos' }),  mimetype='application/json')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)



if __name__ == '__main__':
    app.run(port = 3000, debug = True)