from flask import Flask,jsonify,render_template,request
#Flask->Servidor de flask,jsonify->Usar diccionarios como json ,render_template -> lEER TEMPLATES ,request-> Recibir peticiones


app = Flask(__name__)

from products import products


@app.route('/')
def http():
    return render_template("http.html")

@app.route('/json')#Se define la ruta /json
def json():
    return jsonify({ "Mensaje" : "Mensaje desde objeto json"})

@app.route('/ping')#Se define la ruta de /ping
def ping():
    return "Server works"

@app.route('/ping/<string:msg>')#Se define la ruta de /ping
def ping2(msg):
    return jsonify({"Mensaje por medio de la url":msg})

@app.route('/products/<string:variable>')#esperamos una variable desde el cliente
def getProductsvar(variable):
    prod_encontrado=[ prod for prod in products if prod['Name'] == variable]
    if(len(prod_encontrado)>0):
        return jsonify(prod_encontrado[0])
    return jsonify({"Mensaje":"Producto no encontrado"})

@app.route('/products',methods=["GET"])#Indica  que metodos http se usaran
def getProducts():
    return jsonify({"Productos":products})


@app.route('/products',methods=['POST'])#Indica  que metodos http se usaran
def addProducto():
    newProduct={
        "Name": request.json['Name'],
        "Price":request.json['Price'],
        "Quantity":request.json['Quantity']
    }
    products.append(newProduct)
    return jsonify({"Mensaje":"Productos agregados","Productos":products})


if __name__ == '__main__':
    app.run(debug=True , port=5000)