
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/procesar1', methods=['POST'])
def procesar1():
    name = request.form['name']
    age = int(request.form['age'])
    quantity = int(request.form['quantity'])
    price_per_can = 9000
    total = price_per_can * quantity
    discount = 0

    if 18 <= age <= 30:
        discount = 0.15
    elif age > 30:
        discount = 0.25

    total_discounted = total * (1 - discount)
    return f"Nombre: {name}, Total sin descuento: ${total}, Total con descuento: ${total_discounted:.2f}"

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar2', methods=['POST'])
def procesar2():
    username = request.form['username']
    password = request.form['password']

    users = {
        'juan': 'admin',
        'pepe': 'user'
    }

    if username in users and users[username] == password:
        role = "administrador" if username == "juan" else "usuario"
        return f"Bienvenido {role} {username}"
    else:
        return "Usuario o contraseña incorrectos"

if __name__ == '__main__':
    app.run(debug=True)
