from flask import Flask


from flask import Flask, request
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/sensor", methods=['POST'])
def valor():
    Sensor= request.json['Nombre']
    Valor= request.json['Valor']
    print(f"{Sensor} y {Valor}")
    return "ok"