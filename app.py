import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g, make_response, session, escape, Response,json
import modules.authentication as authentication
from flask_mysqldb import MySQL
import modules.customhash as customhash
import modules.usuarios as usuarios
import mysql.connector
import ast
import logging



app = Flask(__name__)


mydb = mysql.connector.connect(
    host="localhost",
    user="dibankaops",
    password="37f75cac-bcbd-11ea-a5ee-00090ffe0001",
    database="casaBlanca")

logger= None
def Initial():
    global app, mysql, logger
    try:
        #Configuración logger de errores
        logger = logging.getLogger('CasaBlanca')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        handler = logging.FileHandler('casaBlanca_error.log')
        handler.setLevel(logging.ERROR)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        app.secret_key = "RGlCYW5rYTEuMCB3YXMgbWFkZSBmb3IgQ0FTVVIsIGFuZCB3cml0dGVuIGJ5IE1pZ3VlIGFuZCBEYW5pZWwuIEF0IHRoZSBlbmQgb2YgdGhlIHByb2plY3QsIEp1YW4sIEVkd2luLCBIdWdvIGFuZCBBbmRyw6lzIGpvaW5lZCB0aGUgdGVhbS4gTm93IHdlIGFyZSBhIGZpcmVmaWdodGVycyB0ZWFtLg=="
    except Exception as error:
        logger.exception(error)


Initial()
@app.route('/')
def login():
    try:
        return render_template('login.html')
    except Exception as error:
            logger.exception(error)


@app.route('/loginVerify', methods=["GET", "POST"])
def loginVerify():
    try:
        id = request.form['identificacion']
        contra = request.form['contraseña']
        session["username"] = id
        authenticateResponse = authentication.authenticate(id, contra)
        if (authenticateResponse):
            redirect(url_for(authenticateResponse.url))
    except Exception as error:
            logger.exception(error)


@app.route('/home')
def home():
    try:
        # if "adminSuper" in session or "adminSuper" in session: 
            
            return render_template('index.html')
        # return render_template("403.html")
    except Exception as error:
            logger.exception(error)

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
        if "adminSuper" in session or "adminSuper" in session or "ventas" in session:  
            cur = mydb.cursor(dictionary=True)
            cur.execute('''
                    SELECT idProducto, nombreProducto ,precioProducto , fechaProducto FROM productos
                    ''')
            
            productos = cur.fetchall()
            productos = json.dumps(productos)        
            return render_template('homePorductos.html',productos=productos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/ingresoProductos')
def ingresoProductos():
    try:
        cur = mydb.cursor()
        cur.execute('''
                SELECT idProducto, nombreProducto ,precioProducto , fechaProducto,cantidadProducto, valorUnidadProducto, valorTotalProducto,actualizarProducto FROM productos
                ''')
        productos = cur.fetchall()
        return render_template('ingresoProductos.html',productos=productos)
    except Exception as error:
        logger.exception(error)


@app.route('/salidaProductos')
def salidaProductos():
    try:
        cur = mydb.cursor()
        cur.execute('''
                SELECT idProducto, nombreProducto ,precioProducto , fechaProducto FROM productos
                ''')
        productos = cur.fetchall()
        return render_template('salidaProductos.html',productos=productos)
    except Exception as error:
        logger.exception(error)


@app.route('/cortecias')
def cortecias():
    try:
    
        if "adminSuper" in session or "adminSuper" in session: 
            cur = mydb.cursor(dictionary=True)
            cur.execute('''
                    SELECT nombreProducto ,precioProducto ,idProducto FROM productos
                    ''')
            productos = cur.fetchall()
            productos = json.dumps(productos)
            return render_template('cortecias.html',productos=productos)
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/facturaProducto',methods=['POST','GET'])
def facturaProducto():
    try:
        if "adminSuper" in session or "adminSuper" in session or  "ventas" in session: 
            totalVenta = request.form['totalVenta']
            productos = request.form['productos']
            productos = ast.literal_eval(productos)
            idProducto = productos[0]
            contar = 0
            idDetalle=0
            cur = mydb.cursor()
            cur.execute('''
                    INSERT INTO casablanca.facturas (totalFacturas,fechaFactura) VALUES (%s,now())
                    ''',(totalVenta,) )
            
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
                    UPDATE casablanca.detalle SET cantidadDetalle = %s WHERE (idDetalle = %s)
                    ''', (contar,idDetalle,))

                    idDetalle =idDetalle 
                else:
                    cur.execute('''
                        INSERT INTO casablanca.detalle (idFacturaDetalle, idProductoDetalle, cantidadDetalle, fechaDetalle) VALUES (%s, %s, %s, now())
                        ''', (idFactura,producto,contar))

                    idDetalle = cur.lastrowid
            mydb.commit()
            
            return redirect(url_for('ingresoProductos'))
        return render_template("403.html")
    except Exception as error:
        logger.exception(error)


@app.route('/facturarCadaProducto',methods=['POST','GET'])
def facturarCadaProducto():
    try:
        idProdcto = request.form['idProdcto']
        
    except Exception as error:
        logger.exception(error)


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')

if __name__ == '__main__':
    app.run(port = 3000, debug = True)