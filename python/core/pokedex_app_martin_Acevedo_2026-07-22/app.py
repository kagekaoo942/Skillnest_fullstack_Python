import os
from flask import Flask, render_template

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

# Base de datos ficticia de Pokémon ACTUALIZADA
pokedex = [
   {
       "id": 1, 
       "nombre": "Bulbasaur", 
       "tipos": ["Planta", "Veneno"], 
       "habilidades": ["Espesura", "Clorofila"], 
       "imagen": "bulbasaur.png", 
       "poder": 45, 
       "poder_porcentaje": 45, 
       "altura": "0.7", 
       "peso": "6.9"
   },
   {
       "id": 4, 
       "nombre": "Charmander", 
       "tipos": ["Fuego"], 
       "habilidades": ["Mar Llamas", "Poder Solar"], 
       "imagen": "charmander.png", 
       "poder": 39, 
       "poder_porcentaje": 39, 
       "altura": "0.6", 
       "peso": "8.5"
   },
   {
       "id": 7, 
       "nombre": "Squirtle", 
       "tipos": ["Agua"], 
       "habilidades": ["Torrente", "Cura Lluvia"], 
       "imagen": "squirtle.png", 
       "poder": 44, 
       "poder_porcentaje": 44, 
       "altura": "0.5", 
       "peso": "9.0"
   },
   {
       "id": 25, 
       "nombre": "Pikachu", 
       "tipos": ["Eléctrico"], 
       "habilidades": ["Electricidad Estática", "Pararrayos"], 
       "imagen": "pikachu.png", 
       "poder": 35, 
       "poder_porcentaje": 35, 
       "altura": "0.4", 
       "peso": "6.0"
   },
   {
       "id": 39, 
       "nombre": "Jigglypuff", 
       "tipos": ["Normal", "Hada"], 
       "habilidades": ["Gran Encanto", "Tenacidad"], 
       "imagen": "jigglypuff.png", 
       "poder": 115, 
       "poder_porcentaje": 100, 
       "altura": "0.5", 
       "peso": "5.5"
   },
   {
       "id": 52, 
       "nombre": "Meowth", 
       "tipos": ["Normal"], 
       "habilidades": ["Recogida", "Experto"], 
       "imagen": "meowth.png", 
       "poder": 40, 
       "poder_porcentaje": 40, 
       "altura": "0.4", 
       "peso": "4.2"
   },
   {
       "id": 54, 
       "nombre": "Psyduck", 
       "tipos": ["Agua"], 
       "habilidades": ["Humedad", "Aclimatación"], 
       "imagen": "psyduck.png", 
       "poder": 50, 
       "poder_porcentaje": 50, 
       "altura": "0.8", 
       "peso": "19.6"
   },
   {
       "id": 94, 
       "nombre": "Gengar", 
       "tipos": ["Fantasma", "Veneno"], 
       "habilidades": ["Cuerpo Maldito"], 
       "imagen": "gengar.png", 
       "poder": 60, 
       "poder_porcentaje": 60, 
       "altura": "1.5", 
       "peso": "40.5"
   },
   {
       "id": 95, 
       "nombre": "Onix", 
       "tipos": ["Roca", "Tierra"], 
       "habilidades": ["Cabeza Roca", "Robustez"], 
       "imagen": "onix.png", 
       "poder": 35, 
       "poder_porcentaje": 35, 
       "altura": "8.8", 
       "peso": "210.0"
   },
   {
       "id": 143, 
       "nombre": "Snorlax", 
       "tipos": ["Normal"], 
       "habilidades": ["Inmunidad", "Sebo"], 
       "imagen": "snorlax.png", 
       "poder": 160, 
       "poder_porcentaje": 100, 
       "altura": "2.1", 
       "peso": "460.0"
   }
]

# Ruta para mostrar todos los Pokémon al inicio
@app.route("/")
def index():
    return render_template("pokemon.html", pokemons=pokedex)

# Error cuando no se encuentra un Pokémon
def pokemon_no_encontrado(mensaje: str):
    """Función simple para renderizar la página 404 con un mensaje."""
    return render_template("404.html", mensaje=mensaje), 404

@app.route('/pokemon/<busqueda>')
def ver_pokemon(busqueda):
    for p in pokedex:
        if str(p['id']) == busqueda or p['nombre'].lower() == busqueda.lower():
            return render_template('pokemon.html', pokemons=[p])
    
    return pokemon_no_encontrado(f"No existe: {busqueda}")

if __name__ == "__main__":
    app.run(debug=True)