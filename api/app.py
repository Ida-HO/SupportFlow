"""
Aplicación principal de la API de Tickets.
"""
from flask import Flask 
from controllers.tecnico_controller import tecnico_api 
from controllers.usuario_controller import usuario_api 
from controllers.ticket_controller import ticket_api 
from controllers.ticket_historial_controller import ticket_historial_api 

app = Flask(__name__)

app.register_blueprint(tecnico_api)
app.register_blueprint(usuario_api)
app.register_blueprint(ticket_api)
app.register_blueprint(ticket_historial_api)

@app.get("/")
def home():
    """Endpoint raíz para verificar funcionamiento de la API."""
    return {"Api": "API Tickets funcionando. OK"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
