import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g, make_response, session, escape, Response,json
import modules.authentication as authentication
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
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

UPLOAD_FOLDER = None

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

        UPLOAD_FOLDER = os.path.abspath("./static/img/")

        app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
        app.config["FORMATO_PERMITIDO"] = ["PNG", "JPG", "JPEG", "PDF", "DOCX", "DOC"]
        app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024
    except Exception as error:
        logger.exception(error)

def clearSession():
        # Para mas seguridad, al cargar la landingpage siempre se limpian todas las cookies
    session.clear()


Initial()
def archivo_permitido(filename):
        if not "." in filename:
                return False
        
        ext = filename.rsplit(".", 1)[1]

        if ext.upper() in app.config["FORMATO_PERMITIDO"]:
                return True
        else:
                return False




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
            if (authenticateResponse):
                if (authenticateResponse.redirect == True):
                    return redirect(authenticateResponse.url)
                else:
                    mensaje = 'Hay un error en la validacion'
                    return render_template('login.html', mensaje=mensaje)
            else:
                mensaje = 'Hay un error en la validacion'
                return render_template('login.html', mensaje=mensaje)
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
            cur = mydb.cursor()
            # Gastos
            cur.execute('''SELECT  valorGasto FROM gastos where estadoGasto=1 ''')
            gastosDiarios = cur.fetchall()
            sumaGastos = 0
                        
            for gastosDiario in gastosDiarios:
                gastosDiario= gastosDiario[0]
                sumaGastos += gastosDiario

            # Ventas
            cur.execute('''SELECT  totalFacturas FROM facturas where estadoFactura=1 ''')
            totalFacturas = cur.fetchall()
            sumaFacturas = 0
                        
            for totalFactura in totalFacturas:
                totalFactura= totalFactura[0]
                sumaFacturas += totalFactura

            # venta Mes
            cur.execute('''SELECT  totalFacturas FROM facturas where estadoFactura=2 ''')
            facturasMes = cur.fetchall()
            sumaFacturasMes = 0
                        
            for facturaMes in facturasMes:
                facturaMes= facturaMes[0]
                sumaFacturasMes += facturaMes
            
            # Gastos Mes
            cur.execute('''SELECT  valorGasto FROM gastos where estadoGasto=2 ''')
            gastosMes = cur.fetchall()
            sumaGastosMes = 0
                        
            for gastosMes in gastosMes:
                gastosMes= gastosMes[0]
                sumaGastosMes += gastosMes
            
            # Ganancias
            ganancias = sumaFacturasMes - sumaGastosMes
            return render_template('index.html', gastosDiarios=sumaGastos, sumaFacturas=sumaFacturas,sumaFacturasMes=sumaFacturasMes , ganancias=ganancias,sumaGastosMes=sumaGastosMes)
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
            cur.execute('''SELECT idProducto, nombreProducto ,precioProducto , fechaProducto,imagenProducto FROM productos where cantidadProducto > 0''')
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
                            valorTotalProducto
                            FROM productos''')
            productos = cur.fetchall()
            cur.close()
            return render_template('ingresoProductos.html',productos=productos)
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

                cur.execute('''SELECT cantidadProducto FROM productos WHERE  idProducto =%s ''',(idProducto,))
                productos = cur.fetchone()
                if productos[0] > 0:
                    if contar > 1:
                        cur.execute(''' UPDATE detalle 
                                        SET cantidadDetalle = %s 
                                        WHERE (idDetalle = %s)
                        ''', (contar,idDetalle,))

                        contarMenos = productos[0] - 1

                        cur.execute(''' UPDATE productos 
                                        SET cantidadProducto = %s 
                                        WHERE (idProducto = %s)
                        ''', (contarMenos,idProducto,))

                        idDetalle =idDetalle 
                    else:
                        cur.execute(''' INSERT INTO 
                                        detalle
                                        (idFacturaDetalle, idProductoDetalle, 
                                        cantidadDetalle, fechaDetalle) 
                                        VALUES (%s, %s, %s, now())''', 
                                        (idFactura,producto,contar))
                        
                        contarMenos = productos[0] - 1
                        idDetalle = cur.lastrowid

                        cur.execute(''' UPDATE productos 
                                        SET cantidadProducto = %s 
                                        WHERE (idProducto = %s)
                        ''', (contarMenos,idProducto,))


                        
                else:
                    pass
            mydb.commit()
            cur.close()
            return  Response(json.dumps({'error': 'true','page': '/homePorductos',}),  mimetype='application/json')
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
            cur.execute('''SELECT idFactura,totalFacturas,fechaFactura,usuarioFactura,estadoFactura FROM facturas ORDER BY fechaFactura DESC''')
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
            nombreProducto=request.form.get('nombreProducto')
            precioProducto=request.form.get('precioProducto')
            cantidadNueva=request.form.get('cantidadNueva')
            valorNueva=request.form.get('valorNueva')
            valorT = int(valorNueva) * int(cantidadNueva)
            
            if "file" in request.files:
                imagen = request.files.get("file")
                
                if imagen and archivo_permitido(imagen.filename): 
                    filename = secure_filename(imagen.filename)
                    imagen.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                else:
                    message= "El archivo no es una image"
                    return Response(json.dumps({'error': 'true','message':message,'page': '/ingresoProductos' }),  mimetype='application/json')
            else:
                message= "No existe imagen"
                return Response(json.dumps({'error': 'true','message':message,'page': '/ingresoProductos' }),  mimetype='application/json')

            cur = mydb.cursor()
            cur.execute(''' INSERT INTO 
                            productos 
                            (nombreProducto, 
                            precioProducto,cantidadProducto, 
                            valorUnidadProducto, valorTotalProducto,fechaProducto,imagenProducto)
                            VALUES (%s,%s,%s,%s,%s,now(),%s) ''',
                    (nombreProducto, precioProducto, cantidadNueva, valorNueva,valorT,filename))
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


#Gastos
@app.route('/gastos')
def gastos():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur = mydb.cursor()
            cur.execute(''' SELECT idgGasto, nombreGasto,DescipcionGasto,valorGasto, fechaGasto,estadoGasto FROM gastos''')
            gastos = cur.fetchall()
            cur.close()
            return render_template('gastos.html',gastos=gastos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/nuevoGasto',methods=['POST','GET'])
def nuevoGasto():
    try:
        if "adminSuper" in session or "admin" in session: 
            nombreGasto=request.form['nombreGasto']
            descripcionGasto=request.form['descripcionGasto']
            valorGasto=request.form['valorGasto']

            cur = mydb.cursor()

            cur.execute(''' INSERT INTO 
                            gastos 
                            (nombreGasto,
                            DescipcionGasto,
                            valorGasto,
                            fechaGasto,
                            estadoGasto)
                            VALUES (%s,%s,%s,now(),'1') ''',
                            (nombreGasto, descripcionGasto, valorGasto))
            mydb.commit()
            cur.close()
            return Response(json.dumps({'error': 'false','page': '/home' }),  mimetype='application/json')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/editarGasto/<id>',methods=['POST','GET'])
def editarGasto(id):
    try:
        if "adminSuper" in session or "admin" in session: 
            cur = mydb.cursor()
            cur.execute('''SELECT idgGasto, nombreGasto,DescipcionGasto,valorGasto FROM gastos Where idgGasto=%s''',(id,))
            gastos = cur.fetchall()
            cur.close()
            return render_template('editarGasto.html',gastos=gastos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/updateGasto/<id>',methods=['POST','GET'])
def updateGasto(id):
    try:
        if "adminSuper" in session or "admin" in session: 
            nombreGasto=request.form['nombreGasto']
            DescipcionGasto=request.form['DescipcionGasto']
            valorGasto=request.form['valorGasto']

            cur = mydb.cursor()
            
            cur.execute(''' UPDATE 
                            gastos SET 
                            nombreGasto = %s
                            DescipcionGasto = %s, 
                            valorGasto = %s, 
                            fechaUsuario = now()
                            WHERE (idgGasto =%s)''',
                            (nombreGasto, DescipcionGasto, valorGasto ,id))
            mydb.commit()
            cur.close()
            return Response(json.dumps({'error': 'false','page': '/gastos' }),  mimetype='application/json')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/deleteGasto/<id>', methods=['POST'])
def deleteGasto(id):
    try:
        if "adminSuper" in session or "admin" in session: 
            cur =mydb.cursor()
            cur.execute('DELETE FROM gastos WHERE idgGasto =%s',(id,))
            mydb.commit()
            cur.close()
            return redirect(url_for('home'))
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/ventaDia', methods=['POST','GET'])
def ventaDia():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur =mydb.cursor()
            cur.execute('SELECT  idFactura FROM facturas where estadoFactura=1 ')
            facturas = cur.fetchall()
            
            for factura in facturas:
                id = factura[0]
                cur.execute('''UPDATE facturas SET estadoFactura = '2' WHERE (idFactura = %s)''',(id,))


            mydb.commit()
            cur.close()
            return redirect('home')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)

@app.route('/gastosDia', methods=['POST','GET'])
def gastosDia():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur =mydb.cursor()
            cur.execute('SELECT  idgGasto FROM gastos where estadoGasto=1 ')
            gastos = cur.fetchall()
            
            for gasto in gastos:
                id = gasto[0]
                cur.execute('''UPDATE gastos SET estadoGasto = '2' WHERE (idgGasto = %s)''',(id,))


            mydb.commit()
            cur.close()
            return redirect('home')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/ventaMes', methods=['POST','GET'])
def ventaMes():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur =mydb.cursor()
            cur.execute('SELECT  idFactura FROM facturas where estadoFactura=2 ')
            facturas = cur.fetchall()
            
            for factura in facturas:
                id = factura[0]
                cur.execute('''UPDATE facturas SET estadoFactura = '3' WHERE (idFactura = %s)''',(id,))


            mydb.commit()
            cur.close()
            return redirect('home')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)

@app.route('/gastosMes', methods=['POST','GET'])
def gastosMes():
    try:
        if "adminSuper" in session or "admin" in session: 
            cur =mydb.cursor()
            cur.execute('SELECT  idgGasto FROM gastos where estadoGasto=2 ')
            gastos = cur.fetchall()
            
            for gasto in gastos:
                id = gasto[0]
                cur.execute('''UPDATE gastos SET estadoGasto = '3' WHERE (idgGasto = %s)''',(id,))


            mydb.commit()
            cur.close()
            return redirect('home')
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)