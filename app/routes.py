from flask import Blueprint, render_template, Flask

main = Blueprint("main", __name__)

@main.route('/')
def home():
    return render_template('home.html', title='Home')

@main.route("/<path:path>")
def jax_services(path):
    return render_template('home.html')

@main.route('/sobre')
def sobre():
    return render_template('sobre.html', title='Sobre')

@main.route('/galeria')
def galeria():
    return render_template('galeria.html', title='Galeria')

@main.route('/contato')
def contato():
    return render_template('contato.html', title='Contato')
